from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Note


def send_message(request):
    return HttpResponse("Hello from Notes app")


def index(request):
    return render(request, "index.html")


def show_notes(request):
    notes = Note.objects.all()
    return render(request, "index.html", {"notes": notes})


def create_notes(request):
    Note.objects.create(
        title="Monday",
        text="Start your week with a healthy breakfast to stay energized.",
        reminder=datetime(2023, 10, 10),
    )
    Note.objects.create(
        title="Tuesday",
        text="Don't forget to take out the trash to keep your space clean.",
        reminder=datetime(2023, 10, 11),
    )
    Note.objects.create(
        title="Wednesday",
        text="Hit the gym and stay active for a healthy lifestyle.",
        reminder=datetime(2023, 10, 12),
    )
    Note.objects.create(
        title="Thursday",
        text="Make sure to refuel your car for your upcoming journeys.",
        reminder=datetime(2023, 10, 13),
    )
    Note.objects.create(
        title="Friday",
        text="Plan a fun get-together with friends for a great start to the weekend.",
        reminder=datetime(2023, 10, 14),
    )
    Note.objects.create(
        title="Saturday",
        text="Spend quality time with your family and go for a picnic in the park.",
        reminder=datetime(2023, 10, 15),
    )
    Note.objects.create(
        title="Sunday",
        text="Enjoy a relaxing day at home with your loved ones, watching movies and playing board games.",
        reminder=datetime(2023, 10, 16),
    )

    return HttpResponse("Notes created")
