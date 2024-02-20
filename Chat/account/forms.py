from django import forms
from .models import *

class AddUserForm(forms.Form):
    Login = forms.CharField(max_length=20)
    Email = forms.EmailField()
    Password = forms.CharField(min_length=10, max_length=100)
    Confirm_password = forms.CharField(min_length=10, max_length=100) 