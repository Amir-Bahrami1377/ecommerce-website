from django.urls import path
from .views import product_list_api

urlpatterns = [
    path('products/', product_list_api)
]
