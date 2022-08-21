from rest_framework.decorators import api_view

from .utils import get_routes

# Create your views here.


@api_view(["GET"])
def routes_list(request):
    return get_routes(request)
