# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from polls.models import *
from forms import EmployeeForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def polls(request):
    questions = ["How are you?", "Question1?", "Question2?"]
    return render(request, "index.html", {"latest_question_list": questions})


def get_request(request):
    page = request.GET.get("page", None)
    queries = dict(request.GET)
    print(page)
    print(queries)
    return JsonResponse(queries)


def get_object(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404("Not found")
    return HttpResponse(job)


@csrf_exempt
@api_view(["POST"])
def post_request(request):
    data = request.data
    print(data)
    new = Job.objects.create(**data)
    return HttpResponse(new)


@csrf_exempt
@api_view(["PUT"])
def put_request(request, job_id):
    data = request.data
    job = Job.objects.filter(id=job_id)
    job.update(**data)
    return HttpResponse(job.first().min_salary)


@csrf_exempt
@api_view(["DELETE"])
def delete_request(request, job_id):
    job = Job.objects.filter(id=job_id)
    job.delete()
    return HttpResponse("Done")

def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is.valid():
            new = Employee.objects.create(**form.changed_data)
            return HttpResponse(new)
    else:
        form = EmployeeForm()
        return render(request, 'employee.html', {'form': form})



# create
# update:
#   get -> str -> save
#   filter -> update
# delete
# filter(all, first)
# select_related
# bulk_breate
