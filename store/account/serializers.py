from rest_framework import serializers
from .models import Address, Users


class AddressSerializer(serializers.ModelSerializer):
    model = Users
    fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    model = Address
    fields = '__all__'
