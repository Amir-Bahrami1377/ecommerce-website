from django.db import models
from core.models import BaseModel
from product.models import Product, Discount
from account.models import Customer


class OffCode(Discount):
    code = models.CharField(max_length=30, unique=True, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)


class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    off_code = models.OneToOneField(OffCode, on_delete=models.CASCADE, null=True, blank=True)
    final_price = models.IntegerField()


class Basket(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
