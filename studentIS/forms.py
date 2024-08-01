# imports
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, SetPasswordForm
from .models import User, Profile, Student, Address
from django import forms
from django.forms.widgets import DateInput
from .models import SEX_CHOICES

# forms
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["email", "sex", "first_name", "middle_initial", "last_name", "date_of_birth"]
#         labels = {
#             'date_of_birth':'D.O.B',
#             'sex':'sex'
#         }
#         widgets = {
#             'date_of_birth':DateInput(attrs={'type':'date'}),
#             'sex':forms.Select(choices=SEX_CHOICES)
#         }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# Student creation form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["email", "sex", "first_name", "middle_initial", "last_name", "date_of_birth", "SSN", "address"]
        labels = {
            'date_of_birth':'D.O.B',
            'sex':'sex',
            'SSN':'SSN',
        }
        widgets = {
            'date_of_birth':DateInput(attrs={'type':'date'}),
            'sex':forms.Select(choices=SEX_CHOICES),
            'SSN':forms.TextInput(attrs={'type':'text','maxlength':'4','required':'required','pattern':'[0-9]'})
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

