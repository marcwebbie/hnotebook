# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0003_auto_20141026_1903'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bookmarks',
            field=models.ManyToManyField(to='notebooks.Notebook', related_name='bookmarks', blank=True),
            preserve_default=True,
        ),
    ]
