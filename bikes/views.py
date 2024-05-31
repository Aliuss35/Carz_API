from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BikeSerializer
from .models import Bike
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(["GET","POST"])
def get_all_bikes(request):
  if request.method == "GET":
    bike = Bike.objects.all()
    serializer = BikeSerializer(bike, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = BikeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)