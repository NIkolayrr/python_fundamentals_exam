# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-24 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20180823_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
    ]