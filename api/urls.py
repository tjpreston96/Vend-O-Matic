from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_or_refund_coins, name="coins"),
    path('inventory/', views.get_inventory),
    path('inventory/<int:pk>/', views.get_item),
    path("routes/", views.routes_list),
    path('restore/', views.restore),
]
