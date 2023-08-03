from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from dashboard.models import Reservation

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.reservation = Reservation.objects.create(
            customer=self.user,
            date='2023-08-10',
            message='Test reservation',
            status='Pending'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_reservation_view(self):
        response = self.client.get(reverse('reserve_studio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/reserve_studio.html')