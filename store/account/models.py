from django.db import models
from core.models import User, BaseModel


class Customer(User):

    class Meta:
        verbose_name = 'customer'

    def addresses(self):
        return Address.objects.filter(customer__username=self.username)


class Address(BaseModel):
    """
    model for add customer addresses
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=30)
    describe = models.CharField(max_length=120)
