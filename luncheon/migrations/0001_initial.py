# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eatery',
            fields=[
                ('name', models.CharField(help_text="Enter the eatery's name!", max_length=255, primary_key=True, serialize=False, verbose_name='Eatery Name')),
                ('address', models.CharField(max_length=255)),
                ('googleStarRating', models.IntegerField()),
                ('inHouseStarRating', models.IntegerField()),
                ('priceLevel', models.IntegerField()),
                ('hoursOfOperation', models.DurationField()),
                ('link', models.URLField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'ordering': ['inHouseStarRating'],
            },
        ),
    ]
