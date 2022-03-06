from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from account.models import Users
from django.utils.text import slugify


class AbstractDiscount(BaseModel):
    type = models.CharField(max_length=10, choices=[('price', 'price'), ('percent', 'percent')], null=False)
    value = models.PositiveIntegerField(null=False)
    max_price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'type:{self.type} ; value:{self.value}'

    class Meta:
        abstract = True
        ordering = ['-last_updated']


class Category(BaseModel):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'category name:{self.name}'


class Product(BaseModel):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(null=False, default=0)
    description = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(_('Image'), upload_to='uploads/% Y/% m/% d/', null=True, default=None, blank=True)
    stock = models.IntegerField(null=False, default=0)
    brand = models.CharField(max_length=30, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    @property
    def profit_value(self):
        if self.discount:
            if self.discount.type == 'price':
                return min(self.discount.value, self.price)
            else:
                raw_profit = int((self.discount.value / 100) * self.price)
                return int(min(raw_profit, int(self.discount.max_price))) if self.discount.max_price else raw_profit

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name} {self.brand}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        ordering = ['-last_updated']

    def __str__(self):
        return f'product name: {self.name} ; price: {self.price} ; stock: {self.stock}'

    def product_price(self):
        if self.discount.is_active:
            return self.price - self.discount.profit_value(self.price)
        return self.price


class Discount(AbstractDiscount):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
