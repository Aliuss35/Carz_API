from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = ['id', 'make', 'model', 'year', 'price', 'dealership']#you can choose to not include a field in here/ it will not be shown if you delete one
    depth=1