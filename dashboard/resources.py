from import_export import resources,fields
from .models import Product
from .models import Order
from django.contrib.auth.models import User
from datetime import datetime
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('name', 'category', 'sn', 'quantity', 'days')


class OrderResource(resources.ModelResource):



    id = fields.Field(
        column_name='Order Number',
        attribute='id'
    )

    staff_name = fields.Field(
        column_name='Student Name',
        attribute='staff__username'
    )



    product_name = fields.Field(
        column_name='Item',
        attribute='product__name'
    )

    sn = fields.Field(
        column_name='Serial Number',
        attribute='product__sn'
    )

    quantity = fields.Field(
        column_name='Quantity',
        attribute='quantity'
    )


    date = fields.Field(
        column_name='Date Of Order',
        attribute='date'
    )



    class Meta:
        model = Order
        fields = ('id', 'product_name', 'staff_name', 'quantity', 'date','sn')
        column_widths = {
            'id': None,
            'product_name': None,
            'staff_name': None,
            'quantity': None,
            'date': None,
            'sn': None,
        }