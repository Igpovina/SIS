# imports
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, SetPasswordForm
from .models import User, Profile
from django import forms

# forms
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "sex", "password1", "password2"]