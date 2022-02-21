from django.urls import path
from product.views import ProductList

urlpatterns = [
    path('', ProductList.as_view(), name='products')
]
