from django.contrib import admin

from .models import Currency, Item

# Register your models here.
admin.site.register(Currency)
admin.site.register(Item)
