# Generated by Django 4.2.7 on 2023-11-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0013_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="education",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="profile",
            name="profession",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]