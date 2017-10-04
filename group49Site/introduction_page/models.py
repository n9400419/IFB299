from django.db import models

# Create your models here.



class userRegisterAccount(models.Model):
    username = models.CharField(max_length =250)
    password = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250)

    email = models.EmailField(max_length=250)


class login(models.Model):
    userRegisterAccount = models.ForeignKey(userRegisterAccount, on_delete=models.CASCADE)

