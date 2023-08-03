from django.test import TestCase
from django.contrib.auth.models import User
from dashboard.models import Reservation

class ReservationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.reservation = Reservation.objects.create(
            customer=self.user,
            date='2023-08-10',  # Format: yyyy-mm-dd
            message='Test reservation',
            status='Pending'
        )

    def test_reservation_creation(self):
        """Test the creation of a Reservation instance."""
        
        self.assertEqual(self.reservation.customer, self.user)
        self.assertEqual(self.reservation.date, '2023-08-10')
        self.assertEqual(self.reservation.message, 'Test reservation')
        self.assertEqual(self.reservation.status, 'Pending')

    def test_reservation_string_representation(self):
        """Test the __str__ method of the Reservation model."""
        expected_string = f'Studio Reservation on 2023-08-10'
        self.assertEqual(str(self.reservation), expected_string)
