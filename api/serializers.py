from rest_framework.serializers import ModelSerializer

from .models import Currency, Item


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

