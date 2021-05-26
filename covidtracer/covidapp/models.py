from django.db import models

# Create your models here.

class Oxygen(models.Model):
    leadname=models.CharField(max_length=1000)
    agencyname=models.CharField(max_length=10000)
    agencyaddress=models.CharField(max_length=10000000)
    agencyphone=models.CharField(max_length=10)
    verified=models.CharField(max_length=3)

class Pharmacy(models.Model):
    shopname=models.CharField(max_length=10000000)
    address=models.CharField(max_length=100000000)
    number=models.CharField(max_length=10)
    googlemaplink=models.CharField(max_length=1000000000000000000)
    verified=models.CharField(max_length=4)




