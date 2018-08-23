# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Car


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'year', 'price')


admin.site.register(Car, PersonAdmin)
