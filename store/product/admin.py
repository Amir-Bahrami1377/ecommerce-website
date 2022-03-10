from django.contrib import admin
from product.models import Product, Category, Discount


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'stock', 'price', 'brand', 'category', 'image', 'slug', 'is_active', 'is_deleted')
    list_display = ('name', 'stock', 'price', 'is_active', 'brand', 'category', 'slug')
    list_filter = ('name', 'brand', 'category')
    list_display_links = ('name',)
    ordering = ('name', 'brand')
    list_editable = ('is_active',)
    actions = ('deactivate',)
    search_fields = ('name',)

    @admin.action(description='Make selected deactivate')
    def deactivate(self, request, queryset):
        queryset.update(is_active=False)


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('type', 'value', 'max_price', 'is_active', 'product')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'product')


admin.site.register(Discount, DiscountAdmin)
