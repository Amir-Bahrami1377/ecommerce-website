from django.db import models
from core.models import BaseModel


class Customer(BaseModel):
    full_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=14)


class Address(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=30)
    describe = models.CharField(max_length=120)
