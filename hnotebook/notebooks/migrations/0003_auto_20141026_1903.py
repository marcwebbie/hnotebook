# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0002_auto_20141026_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='notebooks',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
