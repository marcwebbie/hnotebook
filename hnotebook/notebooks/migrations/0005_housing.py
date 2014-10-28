# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0004_notebook_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('category', models.CharField(max_length=2, choices=[('RE', 'Rent'), ('BU', 'Buy')], default='RE')),
                ('property_type', models.CharField(max_length=2, choices=[('HO', 'House'), ('FL', 'Flat')], default='FL')),
                ('description', models.TextField()),
                ('town', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('price', models.FloatField()),
                ('caution', models.FloatField(default=0.0)),
                ('guarantee', models.FloatField(default=0.0)),
                ('maintenance_fee', models.FloatField(default=0.0)),
                ('surface', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('elevator', models.BooleanField(default=False)),
                ('num_rooms', models.IntegerField(verbose_name='Rooms')),
                ('num_bedroom', models.IntegerField(verbose_name='Bedrooms')),
                ('num_restroom', models.IntegerField(verbose_name='Restrooms')),
                ('num_living_room', models.IntegerField(verbose_name='Living rooms')),
                ('num_dining_room', models.IntegerField(verbose_name='Dining rooms')),
                ('num_balcony', models.IntegerField(verbose_name='Balconies')),
                ('num_car_park_slot', models.IntegerField(verbose_name='Car park slots')),
                ('kitchen', models.BooleanField(default=False)),
                ('offer_url', models.URLField(default='http://www.example.com')),
                ('notebook', models.ForeignKey(to='notebooks.Notebook')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
