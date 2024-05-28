from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car
from rest_framework import status
from django.shortcuts import get_object_or_404
@api_view(['GET','POST'])
def cars_list(request):
  if request.method == 'GET':
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = CarSerializer(data=request.data)

    if serializer.is_valid()==True:
      serializer.save()
      print(Response(serializer.data))
      return Response(serializer.data)

    else:
      return Response(serializer.errors)

@api_view(["GET","PUT", "DELETE"])
def car_detail(request, pk):#make this same with the <variable> in urls.py
  car = get_object_or_404(Car, pk=pk)

  if request.method == "GET":
    

    serializer = CarSerializer(car)
    return Response(serializer.data)
  
  elif request.method == "PUT":
    serializer=CarSerializer(car, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  elif request.method == "DELETE":
    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)