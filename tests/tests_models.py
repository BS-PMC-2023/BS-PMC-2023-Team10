<<<<<<< HEAD
from django.contrib.auth.models import User
from django.test import TestCase
from user.models import Profile
from dashboard.models import Product,Order

class ProductTestCase(TestCase):
    def setUp(self):
        self.product=Product.objects.create(
            name='HDMI 5M',
            category='Cables',
            quantity=1,
            sn=1234,
        )
    
    def test_product_creation(self):
        """Test the creation of a Product instance."""
        self.assertEqual(self.product.name, 'HDMI 5M')
        self.assertEqual(self.product.category, 'Cables')
        self.assertEqual(self.product.quantity, 1)
        self.assertEqual(self.product.sn, 1234)
    
    def test_product_string_representation(self):
        """Test the __str__ method of the Product model."""
        expected_string = 'HDMI 5M'
        self.assertEqual(str(self.product), expected_string)


       


class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(
            name='HDMI 5M',
            category='Cables',
            quantity=1,
            sn='1234'
           
        )
        self.order = Order.objects.create(
            product=self.product,
            staff=self.user,
            quantity=1,
            returnDate = '2020-12-01'
        )

    def test_order_creation(self):
        """Test the creation of an Order instance."""
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(self.order.staff, self.user)
        self.assertEqual(self.order.quantity, 1)
        self.assertEqual(self.order.returnDate, '2020-12-01')
        




    def test_order_string_representation(self):
        """Test the __str__ method of the Order model."""
        expected_string = 'Order object (1)'
        self.assertEqual(str(self.order), expected_string) 
=======
from django.contrib.auth.models import User
from django.test import TestCase
from user.models import Profile
from dashboard.models import Product,Order
import coverage
cov = coverage.Coverage()
cov.start()
class ProductTestCase(TestCase):
    def setUp(self):
        self.product=Product.objects.create(
            name='HDMI 5M',
            category='Cables',
            quantity=1,
            sn=1234,
        )
    
    def test_product_creation(self):
        """Test the creation of a Product instance."""
        self.assertEqual(self.product.name, 'HDMI 5M')
        self.assertEqual(self.product.category, 'Cables')
        self.assertEqual(self.product.quantity, 1)
        self.assertEqual(self.product.sn, 1234)
    
    def test_product_string_representation(self):
        """Test the __str__ method of the Product model."""
        expected_string = 'HDMI 5M'
        self.assertEqual(str(self.product), expected_string)


       


class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(
            name='HDMI 5M',
            category='Cables',
            quantity=1,
            sn='1234'
           
        )
        self.order = Order.objects.create(
            product=self.product,
            staff=self.user,
            quantity=1,
            returnDate = '2020-12-01'
        )

    def test_order_creation(self):
        """Test the creation of an Order instance."""
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(self.order.staff, self.user)
        self.assertEqual(self.order.quantity, 1)
        self.assertEqual(self.order.returnDate, '2020-12-01')
        




    def test_order_string_representation(self):
        """Test the __str__ method of the Order model."""
        expected_string = 'Order object (1)'
        self.assertEqual(str(self.order), expected_string) 





# Stop coverage
cov.stop()

# Generate the coverage report
cov.report()
>>>>>>> parent of 9c4189f (Merge branch 'main' of https://github.com/BS-PMC-2023/BS-PMC-2023-Team10 into Dana)
