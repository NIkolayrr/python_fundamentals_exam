from django.contrib import admin
from .models import Car


class carAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'year', 'price')


admin.site.register(Car, carAdmin)
