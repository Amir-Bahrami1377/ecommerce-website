from django.contrib import admin
from product.models import Product, Category, Discount, OffCode


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', 'brand', 'category', 'slug')
    list_filter = ('name', 'brand', 'category')
    list_display_links = ('name',)
    ordering = ('name', 'brand')


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('type', 'value', 'max_price', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)


admin.site.register(Discount, DiscountAdmin)


class OffCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'type', 'value', 'max_price', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)


admin.site.register(OffCode, OffCodeAdmin)
