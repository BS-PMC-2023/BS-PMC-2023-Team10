from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from dashboard.models import Product
from dashboard.forms import ProductForm
import coverage
cov = coverage.Coverage()
cov.start()
class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product',quantity=10)
    def test_index_view(self):
        """Test the index view."""
        response = self.client.get(reverse('dashboard-index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')

    def test_staff_view(self):
        """Test the staff view."""
        response = self.client.get(reverse('dashboard-staff'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/staff.html')

    def test_product_view(self):
        """Test the product view."""
        response = self.client.get(reverse('dashboard-product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/product.html')

    def test_product_create_post(self):
        """Test the product create view with a POST request."""
        form_data = {
            'name': 'New Product',
            'quantity': 5
        }
        response = self.client.post(reverse('dashboard-product'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Check for a redirect
        self.assertEqual(Product.objects.count(), 1)  # Verify that a new product was created

   

    

    def test_order_view(self):
        """Test the order view."""
        response = self.client.get(reverse('dashboard-order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/order.html')


cov.stop()

# Generate the coverage report
cov.report()