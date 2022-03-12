from rest_framework import serializers
from order.models import Order, OrderItem, OffCode


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OffCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffCode
        fields = '__all__'
