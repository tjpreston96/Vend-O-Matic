from rest_framework.decorators import api_view

from .utils import (
    add_coin,
    get_item_quantity,
    get_routes,
    inventory_list,
    landing,
    refund_coins,
    vend_item,
)

# Create your views here.


@api_view(["GET"])
def routes_list(request):
    return get_routes(request)


@api_view(["GET","PUT", "DELETE"])
def add_or_refund_coins(request):
    if request.method == 'GET':
        return landing(request)
    if request.method == "PUT":
        return add_coin(request)
    if request.method == "DELETE":
        return refund_coins(request)


@api_view(["GET"])
def get_inventory(request):
    return inventory_list(request)


@api_view(["GET", "PUT"])
def get_item(request, pk):
    if request.method == "GET":
        return get_item_quantity(request, pk)
    if request.method == "PUT":
        return vend_item(request, pk)
