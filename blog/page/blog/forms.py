from django import forms
from .models import Article
from django.forms import ModelForm, TextInput, Textarea, Select, FileInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "summary", "full_text", "category", "slug", "og_image"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "summary": Textarea(
                attrs={"class": "form-control", "placeholder": "Summary"}
            ),
            "full_text": Textarea(
                attrs={"class": "form-control", "placeholder": "Full Text"}
            ),
            "category": Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "slug": TextInput(attrs={"class": "form-control", "placeholder": "Slug"}),
            "og_image": FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "cols": 50}))


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Name", required=True)


class ArticleSearchForm(forms.Form):
    query = forms.CharField(
        label="Search Articles",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Search for articles..."}),
    )
