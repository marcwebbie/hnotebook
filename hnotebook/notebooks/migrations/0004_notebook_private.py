# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0003_auto_20141026_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
