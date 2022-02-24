from django.contrib import admin
from product.models import Product, Category, Discount, OffCode


admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(OffCode)
admin.site.register(Category)
