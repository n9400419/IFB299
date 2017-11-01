from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from accounts.models import *

# Create your tests here.


class AccountsPageTest(TestCase):
    def setUp(self):
        pass

    def test_UserCreationForm_valid(self):

        form = UserCreationForm({'username': "raj", 'email': "raj@yahoo.com", 'user_type': "student", 'password1': "Holiday1",
                      "password2": 'Holiday1', 'family_name': "Rosello", 'given_names': "Raj", 'date_of_birth':"21/21/1995",
                        'address':"123 velors drive", 'phone_number':"0428918729"})

        print(form.errors)
        self.assertTrue(form.is_valid())
