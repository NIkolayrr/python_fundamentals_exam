# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-24 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20180824_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(),
        ),
    ]
