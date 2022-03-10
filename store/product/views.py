from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from product.models import Product, Category


class ProductList(ListView):
    template_name = 'product/products.html'
    model = Product
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'prodslug'

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['prodslug'])


class HomeView(View):
    def get(self, request):
        return render(request, 'product/home.html', {'hi': 'hi'})


class CategoryList(ListView):
    template_name = 'product/category.html'
    model = Category


class CategoryProductList(View):

    def get(self, request, catslug):
        products = Product.objects.filter(category__slug=catslug)
        if products:
            return render(request, 'product/category_product_list.html', context={'products': products})
        else:
            products = Product.objects.filter(category__parent__slug=catslug)
            return render(request, 'product/category_product_list.html', context={'products': products})
