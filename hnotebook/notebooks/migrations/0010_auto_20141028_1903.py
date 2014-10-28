# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0009_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('housing', models.ForeignKey(to='notebooks.Housing')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='model',
            name='housing',
        ),
        migrations.DeleteModel(
            name='Model',
        ),
    ]
