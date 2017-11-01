from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=30, required=True, help_text='Please put number and then street type.')
    date_of_birth = forms.CharField(max_length=50, required=True, help_text="Please put birthday as 'DD/MM/YYYY'")
    phone_number = forms.CharField(max_length=30, required=True,help_text='Please input a valid phone number')
    user_type = forms.CharField(max_length=30, required=True, help_text="Please insert type: 'student', 'businessman', or 'tourist'")


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','user_type', 'email','date_of_birth', 'password1', 'password2', 'address', 'phone_number')



