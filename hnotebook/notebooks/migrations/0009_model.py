# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0008_auto_20141028_0537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('housing', models.ForeignKey(to='notebooks.Housing')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
