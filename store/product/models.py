from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel


class Discount(BaseModel):
    type = models.CharField(max_length=10, choices=[('price', 'price'), ('percent', 'percent')], null=False)
    value = models.PositiveIntegerField(null=False)
    max_price = models.PositiveIntegerField(null=True, blank=True)

    def profit_value(self, price: int):
        if self.type == 'price':
            return min(self.value, price)
        else:
            raw_profit = int((self.value / 100) * price)
            return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit


class Category(BaseModel):
    name = models.CharField(max_length=30)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class Product(BaseModel):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(null=False, default=0)
    description = models.CharField(max_length=120, null=True, blank=True)
    image = models.FileField(_('Image'), null=True, default=None, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField(null=False, default=0)
    brand = models.CharField(max_length=30, null=True, blank=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = _('Products')

    def product_price(self):
        if self.discount.is_active:
            return self.price - self.discount.profit_value(self.price)
        return self.price

    def add_discount(self, discount_id):
        self.discount.pk = discount_id
        self.save()

    def del_discount(self):
        self.discount.deactivate()
