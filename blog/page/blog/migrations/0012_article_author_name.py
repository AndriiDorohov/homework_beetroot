# Generated by Django 4.2.7 on 2023-11-16 23:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_subscribedusers"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="author_name",
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
