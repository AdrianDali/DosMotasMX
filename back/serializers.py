from rest_framework import serializers
from back.models import Product, Category

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

        

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    stock_product = serializers.IntegerField()
    desc = serializers.CharField(max_length=300)
    category = serializers.CharField(max_length=50)
    sell_price = serializers.IntegerField(default=333)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.stock_product = validated_data.get('stock_product', instance.stock_product)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.category = validated_data.get('category', instance.category)
        instance.sell_price = validated_data.get('sell_price', instance.sell_price)
        instance.save()
        return instance
