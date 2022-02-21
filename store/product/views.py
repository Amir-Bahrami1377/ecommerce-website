from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product


class ProductList(ListView):
    template_name = 'product/products.html'
    model = Product
    queryset = Product.objects.filter(is_active=True)
    paginate_by = 10
