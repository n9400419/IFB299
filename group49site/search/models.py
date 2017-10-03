from django.db import models

# Create your models here.

class CityObject(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=50)

    class Meta:
        abstract = True

class College(CityObject):
    departments = models.EmailField(max_length=50)

class Library(CityObject):
    phone_number = models.CharField(max_length=10)
    
class Industry(CityObject):
    industry_type = models.EmailField(max_length=50)
    
class Hotel(CityObject):
    phone_number = models.CharField(max_length=10)
    
class Park(CityObject):
    phone_number = models.CharField(max_length=10)
    a = models.CharField(max_length=1, blank=True, null=True)
    
class Zoo(CityObject):
    phone_number = models.CharField(max_length=10)
    
class Museum(CityObject):
    phone_number = models.CharField(max_length=10)
    
class Restaurant(CityObject):
    phone_number = models.CharField(max_length=10)

class Mall(CityObject):
    phone_number = models.CharField(max_length=10)
