from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta, datetime


class Vehicle(models.Model):
    plate = models.CharField(max_length=15, primary_key=True)
    """
    Plate is a primary key even on their own. Means no need to store any additional field to make rows unique if no any
    specific scenario/requirements exists.
    """

    def __str__(self):
        return self.plate


class Navigation(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_plate = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_navigated = models.DateTimeField()


class Track(models.Model):
    id = models.AutoField(primary_key=True)
    navigation_id = models.ForeignKey(Navigation, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
