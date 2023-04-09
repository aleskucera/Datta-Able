from django.db import models


# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    color = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    online = models.BooleanField(default=False)
