# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def polls(request):
    questions = ["How are you?", "Question1?", "Question2?"]
    return render(request, "index.html", {"latest_question_list": questions})
