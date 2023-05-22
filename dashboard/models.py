from sre_constants import CATEGORY_DIGIT
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
# Create your models here.
CATEGORY = (
    ('Cables','Cables'),
    ('Lights','Lights'),
    ('Convertors','Convertors'),
    ('Projectors','Projectors'),
    ('Tripod','Tripod'),
    ('Apple','Apple'),
    ('Rec','Rec'),
    ('Camera','Camera'),
    )

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    sn = models.CharField(max_length=20, null=True, verbose_name='Serial Number')
    category = models.CharField(max_length=100,choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'
    


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    returnDate = models.DateTimeField(null=False,default=timezone.now,verbose_name='Return Date')
    status = models.CharField(max_length=10, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied'),('Finished', 'Finished')), default='Pending')
    extendRequested = models.CharField(max_length=12, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied'),('NotRequested','NotRequested')), default='NotRequested')
    extendedDate = models.DateTimeField(null=False,default=timezone.now,verbose_name='Extended Date')
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)


    @property
    def day_before_return(self):
        return self.returnDate - timedelta(days=1)
    def current_date(self):
        return timezone.now().date()



