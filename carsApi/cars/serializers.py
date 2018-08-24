from rest_framework import serializers
from .models import Car


class CarSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('url', 'id', 'model', 'year', 'price')
