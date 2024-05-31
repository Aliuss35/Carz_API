from dataclasses import fields
from rest_framework import serializers
from .models import Bike

class BikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bike
    fields = ["id", "make", "model", "year", "price", "cost", "dealership"]
    depth = 1