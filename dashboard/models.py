from sre_constants import CATEGORY_DIGIT
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY = (
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    )


class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    sn = models.PositiveIntegerField(null=True,name='Serial Number')
    category = models.CharField(max_length=100,choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
