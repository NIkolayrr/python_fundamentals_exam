# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
