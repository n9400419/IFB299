from django.db import models

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