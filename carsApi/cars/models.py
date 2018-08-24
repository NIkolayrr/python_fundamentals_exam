from django.db import models


class CarModels(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.ForeignKey(CarModels, on_delete=models.CASCADE)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
