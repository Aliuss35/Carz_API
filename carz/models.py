from django.db import models

# Create your models here. images of of the databases. tables of the database
class Car(models.Model):
  #id column is created by default
  make = models.CharField(max_length=255)
  model = models.CharField(max_length=255)
  year = models.IntegerField()
  price = models.DecimalField(max_digits=8, decimal_places=2)#always use decimalfield with storing the proce values