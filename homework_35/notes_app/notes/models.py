from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateField()

    def __str__(self):
        return self.title
