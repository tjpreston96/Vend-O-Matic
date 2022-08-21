from rest_framework.response import Response


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
