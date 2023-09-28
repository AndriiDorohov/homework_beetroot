from django.db import models

# Create your models here.
import datetime

from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        db_table = "regions"


class Country(models.Model):
    name = models.CharField(max_length=40)
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, related_name="countries"
    )

    class Meta:
        db_table = "countries"

    def __str__(self):
        return f"{self.name} in {self.region}"


class Location(models.Model):
    street_address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=20)
    country = models.ForeignKey(
        Country, on_delete=models.SET_DEFAULT, default=1, related_name="locations"
    )

    class Meta:
        db_table = "locations"


class Job(models.Model):
    JOBS_TITLE = [
        (1, "CEO"),
        (2, "CTO"),
        (3, "Project manager"),
        (4, "Business analytics"),
        (5, "QA"),
        (6, "Designer"),
        (7, "Developer"),
    ]

    title = models.IntegerField(choices=JOBS_TITLE, default=1)
    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()

    class Meta:
        db_table = "jobs"


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    hire_date = models.DateField(auto_now=True)
    salary = models.PositiveIntegerField()

    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey("self", on_delete=models.PROTECT)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

    class Meta:
        db_table = "employees"


class Department(models.Model):
    name = models.CharField(max_length=30)
    manager = models.OneToOneField(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name="department_manager",
    )
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "departments"


class JobHistory(models.Model):
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True)

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = "job_history"
