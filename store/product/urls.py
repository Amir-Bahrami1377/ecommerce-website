from django.urls import path
from product.views import ProductList, ProductDetailView, HomeView


app_name = 'product'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductList.as_view(), name='products'),
    path('<slug:myslug>/', ProductDetailView.as_view(), name='product_detail')
]
