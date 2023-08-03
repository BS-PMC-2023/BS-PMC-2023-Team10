from django.test import TestCase
from dashboard.models import Reservation
from django.contrib.auth.models import User
from datetime import date


class ReservationUserIntegrationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.reservation = Reservation.objects.create(customer=self.user, date=date.today(), message='Test reservation message')

    def test_reservation_user_relationship(self):
        self.assertEqual(self.reservation.customer, self.user)
        self.assertEqual(self.user.reservation_set.count(), 1)
    def test_reservation_str_method(self):
        expected_str = f'Studio Reservation on {self.reservation.date}'
        self.assertEqual(str(self.reservation), expected_str)
