from rest_framework import generics
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorsSerializer, SensorSerializer, MeasurementSerializer

class SensorsView(generics.ListCreateAPIView):
    queryset = Sensor.objects
    serializer_class = SensorsSerializer

class SensorView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects
    serializer_class = SensorSerializer

class MeasurementsView(generics.ListCreateAPIView):
    queryset = Measurement.objects
    serializer_class = MeasurementSerializer