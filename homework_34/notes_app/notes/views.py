from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def send_message(request):
    return HttpResponse("Hello from Notes app.")
