import random
from django.db import models
from django.utils.text import slugify
from core.models import BaseModel
from product.models import Product, AbstractDiscount
from account.models import User, Address


class OffCode(AbstractDiscount):
    verify_code = models.CharField(max_length=30, unique=True, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Order(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    owner_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    off_code = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"slug:{self.slug} ; owner phone number:{self.owner.phone}"

    @property
    def total_price(self):
        order_items = OrderItem.objects.filter(order__slug=self.slug)
        total = 0
        if order_items:
            for item in order_items:
                total += item.price
        return total

    @property
    def final_price(self):
        offcode = OffCode.objects.get(verify_code=self.off_code)
        if offcode:
            final_price = self.total_price - offcode.profit_value(self.total_price)
        else:
            final_price = self.total_price
        return final_price

    def save(self, *args, **kwargs):
        self.slug = slugify(random.randint(10000000, 99999999))
        self.owner_address = Address.objects.get(customer__phone=self.owner.phone, is_default=True)
        super().save(*args, **kwargs)


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"product:{self.product} ; quantity:{self.quantity}"

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        super().save(*args, **kwargs)
