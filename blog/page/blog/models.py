from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user, get_user_model
import os
import pytz


def image_filename(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = f"{instance.title}.{ext}"
    return os.path.join("images", new_filename)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    full_text = models.TextField()
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255, unique=True)
    og_image = models.ImageField(upload_to=image_filename, null=True)
    # is_published = models.BooleanField() #TODO
    likes = models.ManyToManyField(User, related_name="liked_articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_page", kwargs={"slug": self.slug})

    def get_category_url(self):
        return reverse("category_page", kwargs={"category": self.category})

    def save(self, *args, **kwargs):
        user_timezone = pytz.timezone("Europe/Kiev")
        if self.pubdate is None:
            now = timezone.now()
            localized_time = now.astimezone(user_timezone)
            self.pubdate = localized_time

        super().save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
