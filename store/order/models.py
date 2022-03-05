from django.db import models
from core.models import BaseModel
from product.models import Product, AbstractDiscount
from account.models import Users


class OffCode(AbstractDiscount):
    code = models.CharField(max_length=30, unique=True, null=False)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)


class Order(BaseModel):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=False, default=0)
    off_code = models.OneToOneField(OffCode, on_delete=models.CASCADE, null=True, blank=True)
    final_price = models.IntegerField(null=False, default=0)

    def add_amount(self):
        self.amount = 0
        for item in Basket.objects.filter(order=self.pk, is_active=True):
            self.amount += item.basket_item_price()
        self.save()

    def add_final_price(self):
        if self.off_code.is_active:
            self.final_price = self.amount - self.off_code.profit_value(self.amount)
        else:
            self.final_price = self.amount
        self.save()


class Basket(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def basket_item_price(self):
        return self.price * self.quantity
