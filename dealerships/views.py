from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import DealershipSerializer
from .models import Dealership
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(["GET","POST"])
def get_all_dealerships(request):
  if request.method == "GET":

    dealership = Dealership.objects.all()
    serializer = DealershipSerializer(dealership, many=True)
    
    return Response(serializer.data)