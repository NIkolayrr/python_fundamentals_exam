# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import Car, CarModels
from .serializers import CarSerialiser, CarModelSerialiser


class CarList(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerialiser
    http_method_names = ['get', 'post']


class CarModelView(viewsets.ModelViewSet):
    queryset = CarModels.objects.all()
    serializer_class = CarModelSerialiser
