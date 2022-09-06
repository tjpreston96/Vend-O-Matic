from django.test import TestCase

# Extends default client class
from rest_framework.test import APIClient

from .models import Currency, Item
from .views import *

client = APIClient()

# Create your tests here.
class CurrencyTestCase(TestCase):
    def setUp(self) -> None:
        # Currency.objects.create(name="coin")
        self.currency = Currency.objects.create(name="coin")

    def test_currency_creation(self) -> None:
        currency = Currency.objects.first()

        self.assertEqual(len(Currency.objects.all()), 1)
        self.assertEqual(currency.name, "coin")
        self.assertEqual(currency.quantity, 0)

    def test_landing(self) -> None:
        response = client.get("/")
        currency = Currency.objects.first()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.headers["X-Coins"]), currency.quantity)

    def test_add_coin(self) -> None:
        response = client.put("/", {"coin": 1}, format="json")
        currency = Currency.objects.first()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(currency.quantity, 1)
        