from django.db import models

# Create your models here.


class CityObject(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email


class College(CityObject):
    departments = models.TextField(max_length=50)

    def getDepartments(self):
        return self.departments

    
class Library(CityObject):
    phoneNumber = models.CharField(max_length=10)

    def getPhonenumber(self):
        return self.phoneNumber

    
class Industry(CityObject):
    industryType = models.CharField(max_length=20)

    def getIndustryType(self):
        return self.industryType

    
class Hotel(CityObject):
    phoneNumber = models.CharField(max_length=10)

    def getPhoneNumber(self):
        return self.phoneNumber


class CityInformation(CityObject):
    phoneNumber = models.CharField(max_length=10)

    def getPhoneNumber(self):
        return self.phoneNumber

# class Park(CityInformation):
#
#
# class Zoo(CityInformation):
#
#
# class Museum(CityInformation):
#
#
# class Restaurant(CityInformation):
#
#
# class Mall(CityInformation):
#
