from django.db import models
from hnotebook.notebooks.models import Notebook

class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    notebooks = models.ManyToManyField(Notebook, blank=True)
