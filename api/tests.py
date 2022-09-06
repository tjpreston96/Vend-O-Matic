from django.test import TestCase

# Extends default client class
from rest_framework.test import APIClient

from .models import Currency, Item
from .views import *

client = APIClient()

# Create your tests here.
class CurrencyTestCase(TestCase):
    def setUp(self) -> None:
        self.currency = Currency.objects.create(name="coin")

    def test_currency_creation(self) -> None:
        self.assertEqual(len(Currency.objects.all()), 1)
        self.assertEqual(self.currency.name, "coin")
        self.assertEqual(self.currency.quantity, 0)
