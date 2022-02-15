from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel


class Discount(BaseModel):
    type = models.CharField(max_length=10, choices=[('price', 'price'), ('percent', 'percent')], null=False)
    value = models.PositiveIntegerField(null=False)
    max_price = models.PositiveIntegerField(null=True, blank=True)


class Category(BaseModel):
    name = models.CharField(max_length=30)
    parent_id = models.ForeignKey('self', null=True, blank=True)
    discount = models.ManyToManyField(Discount)


class Product(BaseModel):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=120, null=True, blank=True)
    image = models.FileField(_('Image'), null=True, default=None, blank=True)
    discount = models.ManyToManyField(Discount)
    stock = models.IntegerField(null=False)
    brand = models.CharField(max_length=30, null=True, blank=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = _('Products')

    def final_price(self):
        pass
