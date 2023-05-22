from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile
class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='Email (SCE Email Only!)')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

        


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'image','phone']