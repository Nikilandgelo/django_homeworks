from django.urls import path
from stations.views import bus_stations, index

urlpatterns = [
    path('', index),
    path('bus_stations/', bus_stations, name='bus_stations'),
]