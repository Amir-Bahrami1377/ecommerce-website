from django.urls import path
from order.views import CartView
from order.api import OrderItemListCreateApi


app_name = 'orders'
urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('orderitem/', OrderItemListCreateApi.as_view())
]
