from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
