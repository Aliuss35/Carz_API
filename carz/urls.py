from django.urls import path
from . import views

urlpatterns = [
  path('cars/', views.cars_list),
  path('cardetails/<int:pk>/', views.car_detail),#make this same with the <variable> in views.py
]