from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
