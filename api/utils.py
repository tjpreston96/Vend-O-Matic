from rest_framework import status
from rest_framework.response import Response

from .models import Currency, Item
from .serializers import CurrencySerializer, ItemSerializer


def get_routes(request):
    routes = [
        {
            "Endpoint": "/",
            "Method": "PUT",
            "Body": {"coin": 1},
            "Description": "Allows insertion of a single coin (US Quarter) into Vend-O-Matic. Response contains 204 status code and headers containing # of coins accepted.",
        },
        {
            "Endpoint": "/",
            "Method": "DELETE",
            "Body": None,
            "Description": "Vend-O-Matic returns all coins accepted during current transaction. Response contains 204 status code and headers containing # of coins returned.",
        },
    ]

    return Response(routes)


def add_coin(request):
    coin = Currency.objects.first()

    if request.data["coin"] == 1:
        coin.quantity += 1
        coin.save(update_fields=["quantity"])

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            headers={"X-Coins": coin.quantity},
        )

    return Response(
        status=status.HTTP_406_NOT_ACCEPTABLE, headers={"X-Coins": coin.quantity}
    )


# {
#     "coin": 1
# }
