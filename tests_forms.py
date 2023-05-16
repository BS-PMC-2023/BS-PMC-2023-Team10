from django.test import TestCase
from dashboard.forms import ProductForm
from dashboard.models import Product


class ProductFormTestCase(TestCase):
    def test_product_form_valid(self):
        """Test the ProductForm with valid data."""
        form_data = {
            'name': 'Test Product',
            'category': 'Stationary',
            'quantity': 10,
            'sn': 1234,
            'days': '1-2 Days',
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_form_invalid(self):
        """Test the ProductForm with invalid data."""
        form_data = {
            'name': '',  # Invalid, as it's required
            'category': 'Invalid Category',  # Invalid, as it's not in the choices
            'quantity': -5,  # Invalid, as it should be a positive integer
            'sn': 'a', # Invalid, as it should be a positive integer
            'days': '15 Days', # Invalid, as it doesnt have this option.
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_product_form_save(self):
        """Test saving the ProductForm."""
        form_data = {
            'name': 'Test Product',
            'category': 'Stationary',
            'quantity': 10,
            'sn': 1234,
            'days': '1-2 Days',
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

        product = form.save()  # Save the form data to create a Product instance
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.category, 'Stationary')
        self.assertEqual(product.quantity, 10)
        self.assertEqual(product.sn, 1234)
        self.assertEqual(product.days, '1-2 Days')
        
