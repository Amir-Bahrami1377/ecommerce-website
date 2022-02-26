from django.contrib import admin
from account.models import Customer, Address, ProductManager, Operator, Supervisor


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('first_name',)
    list_display_links = ('phone', 'first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', 'phone', 'email')


admin.site.register(Customer, CustomerAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'province', 'city', 'postal_code')
    list_filter = ('customer', 'city')
    list_display_links = ('customer',)
    list_editable = ('postal_code',)
    ordering = ('customer', 'city', 'postal_code')


admin.site.register(Address, AddressAdmin)


class ProductManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('first_name',)
    list_display_links = ('phone', 'first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', 'phone', 'email')


admin.site.register(ProductManager, ProductManagerAdmin)


class OperatorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('first_name',)
    list_display_links = ('phone', 'first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', 'phone', 'email')


admin.site.register(Operator, OperatorAdmin)


class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('first_name',)
    list_display_links = ('phone', 'first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', 'phone', 'email')


admin.site.register(Supervisor, SupervisorAdmin)
