# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerialiser


class CarList(APIView):
    """
    List cars, or create them.
    """
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerialiser(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerialiser
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
