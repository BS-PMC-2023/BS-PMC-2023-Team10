from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Profile(models.Model):
    staff = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(default='avatar.jpg',upload_to='Profile_Images')

    def __str__(self):
        return f'{self.staff.username}-Profile'