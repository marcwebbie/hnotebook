import os
from django.conf import settings
from django.db import models
from hnotebook.notebooks.models import Notebook

class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    picture = models.ImageField(default=os.path.join(settings.STATIC_ROOT,'images','generic-profile-photo.png'))
    notebooks = models.ManyToManyField(Notebook, blank=True)
    bookmarks = models.ManyToManyField(Notebook, blank=True, related_name='bookmarks')
