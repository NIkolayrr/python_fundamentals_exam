# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerialiser


class CarList(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerialiser
    http_method_names = ['get', 'post']
