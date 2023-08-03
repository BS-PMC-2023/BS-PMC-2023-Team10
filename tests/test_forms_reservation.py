from django.test import TestCase
from dashboard.forms import ReservationForm

class ReservationFormTestCase(TestCase):
    def test_reservation_form_valid(self):
        form_data = {
            'date': '2023-08-10',
            'message': 'Test reservation',
        }
        form = ReservationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_reservation_form_invalid(self):
        form_data = {
            'date': '',
            'message': '',
        }
        form = ReservationForm(data=form_data)
        self.assertFalse(form.is_valid())
