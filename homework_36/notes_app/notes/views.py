from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, Category
from django.utils import timezone


def send_message(request):
    return HttpResponse("Hello from Notes app")


def index(request):
    return render(request, "index.html")


def show_notes(request):
    notes = Note.objects.all()
    return render(request, "index.html", {"notes": notes})


# def create_notes(request):
#     health_category, _ = Category.objects.get_or_create(title="Health")
#     household_category, _ = Category.objects.get_or_create(title="Household")
#     automotive_category, _ = Category.objects.get_or_create(title="Automotive")
#     social_category, _ = Category.objects.get_or_create(title="Social")
#     family_category, _ = Category.objects.get_or_create(title="Family")

#     Note.objects.create(
#         title="Monday",
#         text="Start your week with a healthy breakfast to stay energized.",
#         reminder=timezone.make_aware(datetime(2023, 10, 10)),
#         category=health_category,
#     )

#     Note.objects.create(
#         title="Tuesday",
#         text="Don't forget to take out the trash to keep your space clean.",
#         reminder=timezone.make_aware(datetime(2023, 10, 11)),
#         category=household_category,
#     )

#     Note.objects.create(
#         title="Wednesday",
#         text="Hit the gym and stay active for a healthy lifestyle.",
#         reminder=timezone.make_aware(datetime(2023, 10, 12)),
#         category=health_category,
#     )

#     Note.objects.create(
#         title="Thursday",
#         text="Make sure to refuel your car for your upcoming journeys.",
#         reminder=timezone.make_aware(datetime(2023, 10, 13)),
#         category=automotive_category,
#     )

#     Note.objects.create(
#         title="Friday",
#         text="Plan a fun get-together with friends for a great start to the weekend.",
#         reminder=timezone.make_aware(datetime(2023, 10, 14)),
#         category=social_category,
#     )

#     Note.objects.create(
#         title="Saturday",
#         text="Spend quality time with your family and go for a picnic in the park.",
#         reminder=timezone.make_aware(datetime(2023, 10, 15)),
#         category=family_category,
#     )
#     Note.objects.create(
#         title="Sunday",
#         text="Enjoy a relaxing day at home with your loved ones, watching movies and playing board games.",
#         reminder=timezone.make_aware(datetime(2023, 10, 16)),
#         category=family_category,
#     )

#     return HttpResponse("Notes created")
