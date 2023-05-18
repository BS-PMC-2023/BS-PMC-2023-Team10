from django import forms
from .models import Product,Order
from django.forms import TextInput

DAYS_TO_LOAN = (
    ('1-2 Days','1-2 Days'),
    ('3 Days - 1 Week','3 Days - 1 Week'),
    ('1 Week - 2 Weeks','1 Week - 2 Weeks'),
    ('Other','Other'),
    )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity','sn']


class OrderForm(forms.ModelForm):
    days = forms.ChoiceField(choices=DAYS_TO_LOAN, required=True)

    class Meta:
        model = Order
        fields = ['product', 'quantity', 'days']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(quantity__gt=0)