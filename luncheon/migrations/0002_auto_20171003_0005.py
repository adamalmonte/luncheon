# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 04:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luncheon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eatery',
            options={'ordering': ['inHouseStarRating'], 'verbose_name_plural': 'eateries'},
        ),
        migrations.AlterField(
            model_name='eatery',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='eatery',
            name='googleStarRating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Star Rating (Google)'),
        ),
        migrations.AlterField(
            model_name='eatery',
            name='hoursOfOperation',
            field=models.DurationField(blank=True, null=True, verbose_name='Hours of Operation'),
        ),
        migrations.AlterField(
            model_name='eatery',
            name='inHouseStarRating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Star Rating (Fueled)'),
        ),
        migrations.AlterField(
            model_name='eatery',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eatery',
            name='priceLevel',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Price Level'),
        ),
    ]