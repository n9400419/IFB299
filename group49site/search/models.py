from django.db import models

# Create your models here.


class CityObject(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)


    def get_name(self):
        return self.name

    @staticmethod
    def get_city_objects(search_type, object_type, query):
        results = object_type.objects.raw("SELECT * FROM search_" + search_type
                                   + " WHERE name LIKE '%%" + query + "%%'")
        return results

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    class Meta:
        abstract = True


class College(CityObject):
    departments = models.TextField()

    def get_departments(self):
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
    websiteURL = models.CharField(max_length=100)
    info = models.CharField(max_length=200)

    def getPhoneNumber(self):
        return self.phoneNumber

    class Meta:
        abstract = True


class Park(CityInformation):
    pass


class Zoo(CityInformation):
    pass


class Museum(CityInformation):
    pass


class Restaurant(CityInformation):
    pass


class Mall(CityInformation):
    pass

