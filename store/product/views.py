from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from product.models import Product


class ProductList(ListView):
    template_name = 'product/products.html'
    model = Product
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'myslug'

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['myslug'])


class HomeView(View):
    def get(self, request):
        return render(request, 'product/home.html', {'hi': 'hi'})
