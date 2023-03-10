from rest_framework import serializers
from back.models import Product, Category

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)   

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    stock_product = serializers.IntegerField()
    desc = serializers.CharField(max_length=300)
    category = serializers.CharField(max_length=50)
    sell_price = serializers.IntegerField(default=333)


class KitProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)

class KitSerializer(serializers.Serializer): 
    name = serializers.CharField(max_length=150)
    price = serializers.IntegerField()
    stock_kit = serializers.IntegerField()
    desc = serializers.IntegerField()
    category = serializers.CharField()
    sell_price = serializers.IntegerField()
    products = KitProductSerializer(many=True)

class ProductsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    quantity_of_products = serializers.IntegerField()

class KitsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    quantity_of_kits = serializers.IntegerField()

class OrderSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    date = serializers.DateField()
    total = serializers.IntegerField()
    sold = serializers.BooleanField()
    products = ProductsSerializer(many=True)
    kits = KitsSerializer(many=True)

    

    
