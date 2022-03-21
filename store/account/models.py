from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core.models import MyUserManager, BaseModel


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    phone = models.CharField(verbose_name=_('phone'), max_length=11, unique=True,
                             null=False, blank=False)

    deleted = models.BooleanField(default=False)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    delete_timestamp = models.DateTimeField(default=None, null=True, blank=True, editable=False)

    objects = MyUserManager()

    def addresses(self):
        return Address.objects.filter(customer__username=self.username)


class Address(BaseModel):
    """
    model for add customer addresses
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=30)
    describe = models.CharField(max_length=120)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Adresse'
