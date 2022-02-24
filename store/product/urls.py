from product.views import ProductList, ProductDetailView
from django.urls import path


app_name = 'product'
urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<slug:myslug>/', ProductDetailView.as_view(), name='product_detail')
]
