# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 01:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('luncheon', '0007_eatery_favorited_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eatery',
            name='favorited_by',
        ),
        migrations.AddField(
            model_name='eatery',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
