from .models import Article, Comment, Profile

from .forms import (
    ArticleForm,
    CommentForm,
    RegistrationForm,
    LoginForm,
    ArticleSearchForm,
)

from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import DetailView

from bs4 import BeautifulSoup

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers
from django.core.mail import EmailMessage, send_mail
from .forms import NewsletterForm
from .models import SubscribedUsers
from .decorators import user_is_superuser

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


global_context = {
    "author_name": _("Andrii Dorokhov"),
}


def home_page(request):
    articles = Article.objects.all().order_by("-pubdate")
    context = global_context | {"articles": articles}
    page_number = request.GET.get("page", 1)
    items_per_page = 6
    paginated = Paginator(articles, items_per_page)
    try:
        page = paginated.page(page_number)
    except PageNotAnInteger:
        page = paginated.page(1)
    except EmptyPage:
        page = paginated.page(paginated.num_pages)

    specific_article = Article.objects.first()

    show_pagination = paginated.num_pages == 1
    return render(
        request,
        "home_page.html",
        {
            "page": page,
            "specific_article": specific_article,
            **context,
            "show_pagination": show_pagination,
        },
    )


def about_page(request):
    context = global_context
    return render(request, "about_page.html", context)


def single_post_page(request):
    context = global_context
    return render(request, "single_post_page.html", context)


def pages_page(request):
    context = global_context
    return render(request, "pages_page.html", context)


def contact_page(request):
    context = global_context
    return render(request, "contact_page.html", context)


def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    comments = Comment.objects.filter(article=article)
    comment_form = CommentForm()
    full_text_html = BeautifulSoup(article.full_text, "html.parser")
    article_is_liked = request.user in article.likes.all()
    number_of_likes = article.number_of_likes()
    context = global_context | {
        "article": article,
        "comments": comments,
        "comment_form": comment_form,
        "full_text_html": full_text_html,
        "number_of_likes": number_of_likes,
        "article_is_liked": article_is_liked,
    }
    return render(request, "article_page.html", context)


def category_page(request, category):
    articles = Article.objects.filter(category=category)
    context = global_context | {"articles": articles, "category": category}
    return render(request, "category_page.html", context)

def author_page(request, author_name):
    articles = Article.objects.filter(author_name=author_name).order_by("-pubdate")
    context = global_context | {"articles": articles, "author": author_name}
    page_number = request.GET.get("page", 1)
    items_per_page = 6
    paginated = Paginator(articles, items_per_page)
    try:
        page = paginated.page(page_number)
    except PageNotAnInteger:
        page = paginated.page(1)
    except EmptyPage:
        page = paginated.page(paginated.num_pages)

    specific_article = Article.objects.first()

    show_pagination = paginated.num_pages == 1
    return render(
        request,
        "author_page.html",
        {
            "page": page,
            "specific_article": specific_article,
            **context,
            "show_pagination": show_pagination,
        },
    )

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.author_name = request.user.username
            article.save()
            article.likes.set([request.user.id])
            messages.success(request, _("Article has been created successfully."))

            return redirect("home_page")
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = ArticleForm()

    context = global_context | {"form": form}
    return render(request, "create_article.html", context)


def add_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            Comment.objects.create(article=article, user=request.user, text=text)

    return redirect("article_page", slug=article.slug)


def article_like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

    return HttpResponseRedirect(reverse("article_page", args=[article.slug]))


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home_page")
    else:
        form = RegistrationForm()
    return render(request, "./partials/registration.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")
    else:
        form = LoginForm()
    return render(request, "./partials/login.html", {"form": form})


def article_search(request):
    search_form = ArticleSearchForm(request.GET)
    query = request.GET.get("query", "")

    articles = Article.objects.filter(Q(title__icontains=query) | Q(category__icontains=query) | Q(full_text__icontains=query))
    context = {
        "search_form": search_form,
        "articles": articles,
    }

    return render(request, "search_results.html", context)


def subscribe(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)

        if not name or not email:
            messages.error(
                request,
                "You must type legit name and email to subscribe to a Newsletter",
            )
            return redirect("/")

        if User.objects.filter(email=email).exists():
            messages.error(
                request,
                f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.",
            )
            return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(
            request, f"{email} email was successfully subscribed to our newsletter!"
        )
        return redirect(request.META.get("HTTP_REFERER", "/"))


@user_is_superuser
def newsletter(request):
    if request.method == "POST":
        subscribers = SubscribedUsers.objects.all()

        subject = request.POST.get("subject")
        email_message = request.POST.get("message")

        for subscriber in subscribers:
            send_mail(
                subject,
                email_message,
                "your@email.com",
                [subscriber.email],
                fail_silently=False,
            )

        messages.success(request, f"Email sent to all subscribers")
        return redirect("/")

    return render(request, "newsletter.html")


class ArticleDetailView(DetailView):
    model = Article
    # template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        article = get_object_or_404(Article, slug=self.kwargs["slug"])
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        data["total_likes"] = article.total_likes()
        data["article_is_liked"] = liked
        return data


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'partials/register.html', {'form': form})

# Update it here
@login_required
def profile(request):
    user = request.user
    article_count = Article.objects.filter(author=user).count()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            if profile:
                p_form.save()
            else:
                new_profile = p_form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'user': user,
        'article_count': article_count,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'partials/profile_edit.html', context)


@login_required
def profile_view(request):
    user = request.user
    article_count = Article.objects.filter(author=user).count()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            if profile:
                p_form.save()
            else:
                new_profile = p_form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'user': user,
        'article_count': article_count,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'partials/profile_view.html', context)
