from django.db import models

from dealerships.models import Dealership

# Create your models here.
class Bike(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.IntegerField()
    cost = models.DecimalField(max_digits=3, decimal_places=2)#average per 100km
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, default=1)