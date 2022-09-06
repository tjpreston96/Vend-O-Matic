from rest_framework import status
from rest_framework.response import Response

from .models import Currency, Item


def landing(request):
    coins = Currency.objects.first().quantity
    welcome = "Welcome to the Vend-O-Matic Browsable API. To view all possible actions, please navigate to ['/routes']."
    return Response(welcome, status=status.HTTP_200_OK, headers={"X-Coins": coins})


def add_coin(request):
    coin = Currency.objects.first()

    if "coin" in request.data and request.data["coin"] == 1:
        coin.quantity += 1
        coin.save(update_fields=["quantity"])

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            headers={"X-Coins": coin.quantity},
        )

    return Response(
        status=status.HTTP_406_NOT_ACCEPTABLE, headers={"X-Coins": coin.quantity}
    )


def refund_coins(request):
    coin = Currency.objects.first()
    refund = coin.quantity
    coin.quantity = 0
    coin.save(update_fields=["quantity"])
    return Response(status=status.HTTP_204_NO_CONTENT, headers={"X-Coins": refund})


def inventory_list(request):
    inventory = [item.quantity for item in Item.objects.all()]
    return Response(inventory, status=status.HTTP_200_OK)


def get_item_quantity(request, pk):
    item = Item.objects.get(id=pk)
    return Response(item.quantity, status=status.HTTP_200_OK)


def vend_item(request, pk):
    item = Item.objects.get(id=pk)
    coin = Currency.objects.first()
    coins = coin.quantity

    if coins < item.price:
        return Response(status=status.HTTP_403_FORBIDDEN, headers={"X-Coins": coins})
    elif item.quantity == 0:
        return Response(status=status.HTTP_404_NOT_FOUND, headers={"X-Coins": coins})
    else:
        change = coins - item.price
        item.quantity -= 1
        coin.quantity = 0

        item.save(update_fields=["quantity"])
        coin.save(update_fields=["quantity"])

        return Response(
            {"quantity": 1},
            status=status.HTTP_200_OK,
            headers={"X-Coins": change, "X-Inventory-Remaining": item.quantity},
        )


def confirm_restore(request):
    confirmation = "Send 'PUT' request to restore and restock Vend-O-Matic."
    return Response(confirmation, status=status.HTTP_200_OK)


def restock_and_restore(request):
    def restock(item):
        item.quantity = 5
        item.save(update_fields=["quantity"])

    [restock(item) for item in Item.objects.all()]
    inventory = [item.quantity for item in Item.objects.all()]

    coin = Currency.objects.first()
    coin.quantity = 0
    coin.save(update_fields=["quantity"])

    return Response(
        inventory,
        status=status.HTTP_418_IM_A_TEAPOT,
        headers={"X-Coins": coin.quantity},
    )


def get_routes(request):
    routes = [
        {
            "Endpoint": "",
            "Method": "PUT",
            "Body": {"coin": 1},
            "Description": "Allows insertion of a single coin (US Quarter) into Vend-O-Matic. Response contains a 204 status code and headers containing # of coins accepted.",
        },
        {
            "Endpoint": "",
            "Method": "DELETE",
            "Body": None,
            "Description": "Vend-O-Matic returns all coins accepted during current transaction. Response contains a 204 status code and headers containing # of coins returned.",
        },
        {
            "Endpoint": "inventory/",
            "Method": "GET",
            "Body": None,
            "Description": "Vend-O-Matic returns entire remaining inventory. Response contains a 200 status code, and a response body containing a list of integers corresponding to item quanitities.",
        },
        {
            "Endpoint": "inventory/:id",
            "Method": "GET",
            "Body": None,
            "Description": "Vend-O-Matic returns item inventory. Response contains a 200 status code, a response body containing an integer corresponding to individual item quantity.",
        },
        {
            "Endpoint": "inventory/:id",
            "Method": "PUT",
            "Body": None,
            "Description": "Vend-O-Matic vends a beverage to customer. Response contains a 200 status code, a response body containing # of items vended, and headers containing # of coins returned and item inventory remaining.",
        },
        {
            "Endpoint": "restore/",
            "Method": "PUT",
            "Body": None,
            "Description": "Restock and reset Vend-O-Matic. Response contains a 418 status code, a response body containing a list of item quanitities, and headers containing # of coins.",
        },
    ]

    return Response(routes)
