# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profile',
            name='notebooks',
            field=models.ManyToManyField(blank=True, to='notebooks.Notebook'),
            preserve_default=True,
        ),
    ]
