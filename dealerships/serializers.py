from dataclasses import field
from rest_framework import serializers
from .models import Dealership

class DealershipSerializer(serializers.Serializer):
  class Meta:
    model = Dealership
    fields = ["id", "name", "address"]
    depth =1