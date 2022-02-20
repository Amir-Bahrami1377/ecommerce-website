from rest_framework import serializers
from .models import Product, Discount, Category


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    image = serializers.FileField(required=False)
    discount = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all(), required=False, many=True)
    stock = serializers.IntegerField(required=False)
    brand = serializers.CharField(required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, many=True)

    def update(self, instance: Product, validated_data: dict) -> Product:
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        return instance

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)
