from django.test import TestCase
from dashboard.forms import ProductForm
from dashboard.models import Product
import coverage
cov = coverage.Coverage()
cov.start()
class ProductFormTestCase(TestCase):
    def test_product_form_valid(self):
        """Test the ProductForm with valid data."""
        form_data = {
            'name': 'HDMI 5M',
            'category': 'Cables',
            'quantity': 1,
            'sn': '1234',
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
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_product_form_save(self):
        """Test saving the ProductForm."""
        form_data = {
            'name': 'HDMI 5M',
            'category': 'Cables',
            'quantity': 1,
            'sn': '1234',
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

        product = form.save()  # Save the form data to create a Product instance
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, 'HDMI 5M')
        self.assertEqual(product.category, 'Cables')
        self.assertEqual(product.quantity, 1)
        self.assertEqual(product.sn, '1234')
        

# Stop coverage
cov.stop()

# Generate the coverage report
cov.report()