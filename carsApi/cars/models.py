from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

currentYear = datetime.now().year


class CarModels(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.ForeignKey(CarModels, on_delete=models.CASCADE)
    year = models.IntegerField(
        validators=[MaxValueValidator(currentYear), MinValueValidator(1960)]
     )
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
