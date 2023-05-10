from import_export import resources,fields
from .models import Product
from .models import Order
from django.contrib.auth.models import User
from datetime import datetime

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('name', 'category', 'quantity')


class OrderResource(resources.ModelResource):
    product_name = fields.Field(
        column_name='Product',
        attribute='product__name'
    )

    staff_name = fields.Field(
        column_name='Name',
        attribute='staff__username'
    )

    id = fields.Field(
    column_name='ID',
    attribute='id'
    )

    quantity = fields.Field(
    column_name='Quantity',
    attribute='quantity'
    )

    date = fields.Field(
        column_name='Date',
        attribute='date'
    )

    class Meta:
        model = Order
        fields = ('id', 'product_name', 'staff_name', 'quantity', 'date')