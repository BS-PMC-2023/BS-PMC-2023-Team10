from django.contrib.auth.models import User
from django.test import TestCase
from user.models import Profile
from dashboard.models import Product,Order

class ProductTestCase(TestCase):
    def setUp(self):
        self.product=Product.objects.create(
            name='TestProduct',
            category='Stationary',
            quantity=10,
            sn=1234,
            days='1-2 Days',

        )
    
    def test_product_creation(self):
        """Test the creation of a Product instance."""
        self.assertEqual(self.product.name, 'TestProduct')
        self.assertEqual(self.product.category, 'Stationary')
        self.assertEqual(self.product.quantity, 10)
        self.assertEqual(self.product.sn, 1234)
        self.assertEqual(self.product.days, '1-2 Days')
    
    def test_product_string_representation(self):
        """Test the __str__ method of the Product model."""
        expected_string = 'TestProduct'
        self.assertEqual(str(self.product), expected_string)


       


class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(
            name='Test Product',
            category='Stationary',
            quantity=10,
           
        )
        self.order = Order.objects.create(
            product=self.product,
            staff=self.user,
            quantity=5,
        )

    def test_order_creation(self):
        """Test the creation of an Order instance."""
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(self.order.staff, self.user)
        self.assertEqual(self.order.quantity, 5)




    def test_order_string_representation(self):
        """Test the __str__ method of the Order model."""
        expected_string = 'Order object (1)'
        self.assertEqual(str(self.order), expected_string) 
