from django.test import SimpleTestCase
from django.urls import reverse,resolve
from dashboard.views import index,staff,order,product
class TestUrls(SimpleTestCase):
    #Tests for the urls
    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard-index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

        url = reverse('dashboard-staff')
        print(resolve(url))
        self.assertEquals(resolve(url).func, staff)

        url = reverse('dashboard-order')
        print(resolve(url))
        self.assertEquals(resolve(url).func, order)

        url = reverse('dashboard-product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, product)