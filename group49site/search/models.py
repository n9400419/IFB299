from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    departments = models.EmailField(max_length=50)
    email_address = models.EmailField(max_length=50)
    
class Library(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=50)
    
class Industry(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    industry_type = models.EmailField(max_length=50)
    email_address = models.EmailField(max_length=50)
    
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=50)
    
class Park(models.Model):    
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=50)
    
class Zoo(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=50)
    
class Museum(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=50)
    
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=50)
    
class Mall(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=50)
