from django.db import models

# Create your models here.



class Truck(models.Model):
    number_plate = models.CharField(max_length=20, unique=True)
    registration_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.number_plate


class Driver(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    language = models.CharField(max_length=20)
    assigned_truck = models.OneToOneField(Truck, on_delete=models.SET_NULL, null=True, blank=False, related_name='driver')

    def __str__(self):
        return self.name

