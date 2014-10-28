# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notebooks', '0006_housing_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField()),
                ('text', models.TextField()),
                ('commenter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('housing', models.ForeignKey(to='notebooks.Housing')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
