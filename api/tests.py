from django.test import Client, RequestFactory, TestCase

from .models import Currency, Item
from .views import *

c = Client()

# Create your tests here.
class CurrencyTestCase(TestCase):
    def setup(self):
        self.factory = RequestFactory()
        self.currency = Currency.objects.create(name="coin")

    def test_setup(self):
        self.assertEqual(len(Currency.objects.all(), 1))
        self.assertEqual(self.currency.name, "coin")
        self.assertEqual(self.currency.quantity, 0)
