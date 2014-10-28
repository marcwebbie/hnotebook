# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0005_housing'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='currency',
            field=models.CharField(max_length=10, default='$'),
            preserve_default=True,
        ),
    ]
