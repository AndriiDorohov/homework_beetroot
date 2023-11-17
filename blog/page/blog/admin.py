from django.contrib import admin
from .models import Article, SubscribedUsers


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(SubscribedUsers)
class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_date")
