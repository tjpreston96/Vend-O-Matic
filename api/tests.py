from django.test import TestCase

# Extends default Client class
from rest_framework.test import APIClient

from .models import Currency, Item
from .views import *

client = APIClient()

# Create your tests here.
class CurrencyTestCase(TestCase):
    def setUp(self) -> None:
        Currency.objects.create(name="coin")

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

    def test_routes(self) -> None:
        response = client.get("/routes/")
        self.assertEqual(response.status_code, 200)

    def test_invalid_add_coin(self) -> None:
        # Invalid key
        response = client.put("/", {"quarter": 1}, format="json")
        currency = Currency.objects.first()
        self.assertEqual(response.status_code, 406)
        self.assertEqual(currency.quantity, 0)

        # Invalid value
        response = client.put("/", {"coin": 3}, format="json")
        currency = Currency.objects.first()
        self.assertEqual(response.status_code, 406)
        self.assertEqual(currency.quantity, 0)

    def test_valid_add_coin(self) -> None:
        # Single k:v pair
        response = client.put("/", {"coin": 1}, format="json")
        currency = Currency.objects.first()
        self.assertEqual(response.status_code, 204)
        self.assertEqual(currency.quantity, 1)

        # Multiple k:v pairs
        response = client.put("/", {"quarter": 2, "coin": 1, "taco": 1}, format="json")
        currency = Currency.objects.first()
        self.assertEqual(response.status_code, 204)
        self.assertEqual(currency.quantity, 2)

    def test_refund_coins(self) -> None:
        refund = Currency.objects.first().quantity
        response = client.delete("/")
        currency = Currency.objects.first()
        self.assertEqual(response.status_code, 204)
        self.assertEqual(int(response.headers["X-Coins"]), refund)
        self.assertEqual(currency.quantity, 0)


class ItemTestCase(TestCase):
    def setUp(self) -> None:
        # Create Currency w/ quantity of 3
        Currency.objects.create(name="coin", quantity=3)
        # Create 3 Items with quantity of 1
        [Item.objects.create(quantity=1) for i in range(3)]

    def test_item_creation(self) -> None:
        self.assertEqual(len(Item.objects.all()), 3)

    def test_inventory_list(self) -> None:
        response = client.get("/inventory/")
        self.assertEqual(type(response.data), list)
        self.assertEqual(response.status_code, 200)

    def test_get_item_quanity(self) -> None:
        response = client.get("/inventory/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), int)

    def test_vend_item(self) -> None:
        # Successful transaction (200)
        response = client.put("/inventory/10/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(response.headers["X-Coins"]), 1)
        self.assertEqual(int(response.headers["X-Inventory-Remaining"]), 0)

        # Insufficient coins (403)
        response = client.put("/inventory/11/")
        self.assertEqual(response.status_code, 403)
        self.assertEqual(int(response.headers["X-Coins"]), 0)

        # Insert 2 coins
        client.put("/", {"coin": 1}, format="json")
        client.put("/", {"coin": 1}, format="json")

        # Out of stock (404)
        response = client.put("/inventory/10/")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(int(response.headers["X-Coins"]), 2)
