from django.db import models

from django.conf import settings 

APP_LOCATION = settings.DEFAULT_LOCATION

class Job(models.Model):
	title = models.CharField(max_length=128)
	salary = models.IntegerField()
	longitude = models.FloatField()
	latitude = models.FloatField()
