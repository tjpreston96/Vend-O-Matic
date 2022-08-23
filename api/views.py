from rest_framework.decorators import api_view

from .utils import get_quantity, get_routes, add_coin, inventory_list, refund_coins

# Create your views here.


@api_view(["GET"])
def routes_list(request):
    return get_routes(request)


@api_view(["PUT", "DELETE"])
def add_or_refund_coins(request):
    if request.method == "PUT":
        return add_coin(request)
    if request.method == "DELETE":
        return refund_coins(request)


@api_view(["GET"])
def get_inventory(request):
    return inventory_list(request)


@api_view(["GET"])
def get_item(request, pk):
    if request.method == "GET":
        return get_quantity(request, pk)
