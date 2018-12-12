from django.db import models

from django.conf import settings 

APP_LOCATION = settings.DEFAULT_LOCATION

class Job(models.Model):
    title = models.CharField(max_length=128)
    salary = models.IntegerField()
    city = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.city
