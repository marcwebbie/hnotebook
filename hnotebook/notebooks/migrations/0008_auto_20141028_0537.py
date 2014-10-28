# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0007_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='date',
            new_name='datetime',
        ),
    ]
