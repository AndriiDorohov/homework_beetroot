from .models import Article, Comment

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
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import DetailView

from bs4 import BeautifulSoup

global_context = {
    "author_name": _("Andrii Dorokhov"),
}


def home_page(request):
    articles = Article.objects.all().order_by("-pubdate")
    context = global_context | {"articles": articles}
    page_number = request.GET.get("page", 1)
    paginated = Paginator(articles, 2)
    try:
        page = paginated.page(page_number)
    except PageNotAnInteger:
        page = paginated.page(1)
    except EmptyPage:
        page = paginated.page(paginated.num_pages)

    return render(request, "home_page.html", {"page": page, **context})


def about_page(request):
    context = global_context
    return render(request, "about_page.html", context)


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


def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

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
    return render(request, "registration.html", {"form": form})


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
    return render(request, "login.html", {"form": form})


def article_search(request):
    search_form = ArticleSearchForm(request.GET)
    query = request.GET.get("query", "")

    articles = Article.objects.filter(title__icontains=query)

    context = {
        "search_form": search_form,
        "articles": articles,
    }

    return render(request, "search_results.html", context)


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
