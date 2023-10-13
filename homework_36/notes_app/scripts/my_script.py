from notes.models import Category, Note
import os
import django
from datetime import datetime
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes_app.settings")
django.setup()

def run():
    Note.objects.all().delete()
    Category.objects.all().delete()

    category = Category(title="Category Title")
    category.save()

    notes = [
        {
            "title": "Monday",
            "text": "Start your week with a healthy breakfast to stay energized.",
            "reminder": timezone.datetime(2023, 10, 10),
        },
        {
            "title": "Tuesday",
            "text": "Don't forget to take out the trash to keep your space clean.",
            "reminder": timezone.datetime(2023, 10, 11),
        },
        {
            "title": "Wednesday",
            "text": "Hit the gym and stay active for a healthy lifestyle.",
            "reminder": timezone.datetime(2023, 10, 12),
        },
        {
            "title": "Thursday",
            "text": "Make sure to refuel your car for your upcoming journeys.",
            "reminder": timezone.datetime(2023, 10, 13),
        },
        {
            "title": "Friday",
            "text": "Plan a fun get-together with friends for a great start to the weekend.",
            "reminder": timezone.datetime(2023, 10, 14),
        },
        {
            "title": "Saturday",
            "text": "Spend quality time with your family and go for a picnic in the park.",
            "reminder": timezone.datetime(2023, 10, 15),
        },
        {
            "title": "Sunday",
            "text": "Enjoy a relaxing day at home with your loved ones, watching movies and playing board games.",
            "reminder": timezone.datetime(2023, 10, 16),
        },
    ]

    for data in notes:
        note = Note(
            title=data["title"],
            text=data["text"],
            reminder=data["reminder"],
            category=category,
        )
        note.save()
