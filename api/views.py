from rest_framework.decorators import api_view

from .utils import get_routes, add_coin, refund_coins

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
