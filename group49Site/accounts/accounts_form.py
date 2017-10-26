from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=30, required=True, help_text='Please put number and then street type.')
   # date_of_birth = forms.DateField(required=True,help_text='Required. Format: YYYY-DD-MM')
    phone_number = forms.CharField(max_length=30, required=True,help_text='Please input a valid phone number')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address', 'phone_number')



