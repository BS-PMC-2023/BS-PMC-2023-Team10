from django import forms
from .models import Product,Order
from django.forms import TextInput
from django.core.exceptions import ValidationError


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

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity','sn']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['category', 'product', 'quantity', 'returnDate']
        widgets = {
            'returnDate': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.none()

        if 'category' in self.data:
            category = self.data['category']
            self.fields['product'].queryset = Product.objects.filter(category=category, quantity__gt=0)
        elif self.instance.pk:
            category = self.instance.product.category
            self.fields['product'].queryset = Product.objects.filter(category=category, quantity__gt=0)

        self.fields['category'].widget.attrs['onchange'] = 'this.form.submit();'

        # Add available quantity information to the product field widget
        self.fields['product'].widget = forms.Select(
            attrs={'class': 'form-control'},
            choices=[(product.id, f'{product.name} (Available: {product.quantity})') for product in self.fields['product'].queryset]
        )

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        product = cleaned_data.get('product')
        quantity = cleaned_data.get('quantity')

        if category and product and quantity is not None:
            try:
                selected_product = Product.objects.get(category=category, pk=product.id)
            except Product.DoesNotExist:
                raise ValidationError('Invalid product choice.')

            if quantity > selected_product.quantity:
                raise ValidationError('Requested quantity exceeds available quantity.')

        return cleaned_data

    def add_error(self, field, error):
        if field == 'product' and error.code == 'invalid_choice':
            return
        super().add_error(field, error)

    def full_clean(self):
        super().full_clean()
        if 'product' in self._errors:
            self._errors['product'].clear()
            del self._errors['product']