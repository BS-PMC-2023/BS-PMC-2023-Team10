from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class CreateUserForm(UserCreationForm):
    #studentId = forms.ImageField(required=False)
    username = forms.CharField(label='Email (SCE Email Only!)')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


""" def clean_studetID(self):
        studentId = self.cleaned_data['studentId']
        # Implement any validation or checks for the student id field if needed
        return studentId """
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'image','phone']



