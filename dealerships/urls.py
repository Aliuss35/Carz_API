from django.urls import path
from . import views


urlpatterns = [
path("dealerships/", views.get_all_dealerships),
]