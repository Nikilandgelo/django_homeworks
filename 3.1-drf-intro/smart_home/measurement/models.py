from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_measurement')
    temperature = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True)