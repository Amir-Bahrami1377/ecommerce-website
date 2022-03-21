from rest_framework import serializers
from .models import Address, User


class AddressSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    model = Address
    fields = '__all__'
