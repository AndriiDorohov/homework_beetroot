from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_notes, name="notes_list"),
    # path("create_notes/", views.create_notes, name="create_notes"),
]
