# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luncheon', '0005_remove_eatery_hoursofoperation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eatery',
            options={'ordering': ['name'], 'verbose_name_plural': 'eateries'},
        ),
        migrations.RenameField(
            model_name='eatery',
            old_name='link',
            new_name='website_link',
        ),
        migrations.RemoveField(
            model_name='eatery',
            name='inHouseStarRating',
        ),
        migrations.AddField(
            model_name='eatery',
            name='menu_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
