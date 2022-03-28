from dataclasses import Field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile 

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
# Form For User Data
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']

# Form For Profile Date

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['phone_number','image','city']