from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


#
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    class Meta:
        abstract = True


class BusinessMan(UserType):
    current_type = models.IntegerField()

class Student(UserType):
    current_type = models.IntegerField()

class Tourist(UserType):
    current_type = models.IntegerField()










