# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luncheon', '0002_auto_20171003_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatery',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='eatery',
            name='name',
            field=models.CharField(help_text="Enter the eatery's name!", max_length=255, verbose_name='Eatery Name'),
        ),
    ]
