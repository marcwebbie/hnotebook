import os
from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from django.db import models

from hnotebook.notebooks.models import Notebook
from .factories import UserFactory


class Profile(models.Model):
    DEFAULT_PICTURE = os.path.join(settings.STATIC_ROOT,'images','generic-profile-photo.png')

    user = models.OneToOneField(User)
    picture = models.ImageField(default=DEFAULT_PICTURE)
    notebooks = models.ManyToManyField(Notebook, blank=True)
    bookmarks = models.ManyToManyField(Notebook, blank=True, related_name='bookmarks')

    @property
    def username(self):
         return self.user.username

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return '{}, {}'.format(self.username, self.full_name)
