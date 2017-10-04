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










<<<<<<< HEAD
=======
# Create your models here.


class User(models.Model):

    class Meta:
        abstract = True

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=10)
    email = models.EmailField()
    userType = models.CharField(max_length=11)

    searchTypes = []

    def getSearchTypes(self):
        return self.searchTypes

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getAddress(self):
        return self.address

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    def getUserType(self):
        return self.userType


class Tourist(User):
    searchTypes = ['Hotel']


class Student(User):
    searchTypes = ['College', 'Library']


class Businessman(User):
    searchTypes = ['Hotel', 'Industry']
>>>>>>> 070966ab59f18a3469690d39d38d16bd819ec960
