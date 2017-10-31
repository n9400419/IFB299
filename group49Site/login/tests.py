from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from accounts.models import *
from django.core.files import File
from django.contrib import auth
from login.views_login import *


class LoginTest(TestCase):

    def setUp(self):
        pass

    def test_LoginPage(self):
        response = self.client.get('http://127.0.0.1:8000/login/')
        self.assertEqual(response.status_code, 200)

    def test_UsernameTextArea(self):
        response = self.client.get('http://127.0.0.1:8000/login/')
        self.assertContains(response, 'username')

    def test_PasswordTextArea(self):
        response = self.client.get('http://127.0.0.1:8000/login/')
        self.assertContains(response, 'password')

    #Invalid Username
    def test_UserAuthenticateInvalidUsername(self):
        user = User.username.clean('testing')
        user.set_password('12345')
        user.save()
        self.client.post('http://127.0.0.1:8000/login/',{'username': 'ASKDJNQJWKND', 'password': '12345'},follow=True)
        user = auth.get_user(self.client)
        self.assertFalse(user.User.is_authenticated)

    #InValid Password
    def test_UserAuthenticateInValidPassword(self):
        user = User.username.clean('testing')
        user.set_password('12345')
        user.save()
        self.client.post('http://127.0.0.1:8000/login/',{'username': 'testing', 'password': 'XWRONGX'},follow=True)
        user = auth.get_user(self.client)
        self.assertFalse(user.User.is_authenticated())

    #Valid Username
    def test_UserAuthenticateValidUsername(self):
        user = User.username.clean('testing')
        user.set_password('12345')
        user.save()
        self.client.post('http://127.0.0.1:8000/login/',{'username': 'testing', 'password': '12345'},follow=True)
        user = auth.get_user(self.client)
        self.assertTrue(user.User.is_authenticated())

    #Valid Password
    def test_UserAuthenticateValidPass(self):
        user = User.username.clean('testing')
        user.set_password('12345')
        user.save()
        self.client.post('http://127.0.0.1:8000/login/',{'username': 'testing', 'password': '12345'},follow=True)
        user = auth.get_user(self.client)
        self.assertTrue(user.User.is_authenticated())

