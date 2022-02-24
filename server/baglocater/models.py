from django.db import models

# Create your models here.
class Credentials(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class AddLostAndFound(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    flightNumber = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=30)
    baggageNumber = models.CharField(max_length=30)
    departureAirport = models.CharField(max_length=30)
    arrivalAirport = models.CharField(max_length=30)
    departureDate = models.CharField(max_length=30)
    arrivalDate = models.CharField(max_length=30)
    url = models.CharField(max_length=100)