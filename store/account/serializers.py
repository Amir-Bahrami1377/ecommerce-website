from rest_framework import serializers
from .models import Address, Customer


class AddressSerializer(serializers.ModelSerializer):
    model = Customer
    fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    model = Address
    fields = '__all__'
