from django.urls import path
from product.views import ProductList, ProductDetailView, HomeView, CategoryList, CategoryProductList


app_name = 'product'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductList.as_view(), name='products'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('search/category/<slug:catslug>/', CategoryProductList.as_view(), name='category_product_list'),
    path('<slug:prodslug>/', ProductDetailView.as_view(), name='product_detail')
]
