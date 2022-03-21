from django.contrib import admin
from account.models import User, Address


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('first_name',)
    list_display_links = ('phone', 'first_name', 'last_name', 'email')
    ordering = ('first_name', 'last_name', 'phone', 'email')
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'province', 'city', 'postal_code')
    list_filter = ('customer', 'city')
    list_display_links = ('customer',)
    list_editable = ('postal_code',)
    ordering = ('customer', 'city', 'postal_code')


admin.site.register(Address, AddressAdmin)

