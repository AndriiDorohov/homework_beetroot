from django.shortcuts import render
from django.http import HttpResponse


def send_message(request):
    return HttpResponse("Hello from Notes app")


def index(request):
    return render(request, "index.html")
