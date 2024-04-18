from rest_framework import serializers
from measurement.models import Sensor, Measurement

class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    sensor_measurement = MeasurementSerializer(many = True)
    class Meta:
        model = Sensor
        fields = '__all__'