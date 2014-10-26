from django.db import models

class Notebook(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    notebooks = models.ManyToManyField(Notebook, blank=True)
