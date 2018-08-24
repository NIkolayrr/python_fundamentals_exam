from rest_framework import serializers
from .models import Car, CarModels


class CarSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('url', 'id', 'model', 'year', 'price')


class CarModelSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CarModels
        fields = ('url', 'id', 'name')
