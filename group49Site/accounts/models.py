from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email_address = models.EmailField(max_length=50)
    address = models.CharField(max_length=100,default="21 kapa street")
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50)


	
