from django.contrib import admin
from order.models import Order, OrderItem, OffCode


class OrderAdmin(admin.ModelAdmin):
    list_display = ('slug', 'final_price')
    search_fields = ('slug',)
    list_display_links = ('slug',)


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'order')
    list_editable = ('quantity',)
    list_display_links = ('product',)


admin.site.register(OrderItem, OrderItemAdmin)


class OffCodeAdmin(admin.ModelAdmin):
    list_display = ('verify_code', 'type', 'value')
    search_fields = ('verify_code',)
    list_display_links = ('verify_code',)


admin.site.register(OffCode, OffCodeAdmin)
