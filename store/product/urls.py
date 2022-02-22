from django.urls import path
from product.views import ProductList, ProductDetailView


app_name = 'product'
urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<slug:myslug>/', ProductDetailView.as_view(), name='product_detail')
]
