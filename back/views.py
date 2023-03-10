from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from back.serializers import CategorySerializer, ProductSerializer, OrderSerializer, KitSerializer
from back.classes import Category, Product, Order, Kit
from back.models import Product as ProductModel, Category as CategoryModel

# Create your views here.
class TestView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        return Response({"message":"Hello World"},status=status.HTTP_200_OK)
    
class ProductView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        for key in request.data.get('product'):
            serializer = ProductSerializer(data =key)
            serializer.is_valid(raise_exception=True)
            
            data = serializer.validated_data
            
            print(data)

            product = Product( data= data  ) 
            product.insert_db()
        return Response({"message":"Productos dado de alta"},status=status.HTTP_200_OK)
    
    
class OrderView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        serializer = OrderSerializer(data =request.data.get('order'))
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print("######################DATA ORDER######################")
        print(data)
        order = Order(data)
        
        order.insert_db()
        print("######################DATA ORDER######################")
        print(order)

        return Response({"message":"Order created succes"},status=status.HTTP_200_OK)
    
    
class CategoryView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        
        for key in request.data.get('category'):
            serializer = CategorySerializer(data =key)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            category = Category(data.get("name"))
            category.insert_db()      

        return Response({"message":"Category created succes"},status=status.HTTP_200_OK)
    
class KitView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        serializer = KitSerializer(data = request.data.get("kit"))
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print("#####################data para la generacion de un kit")
        print(data)
        kit = Kit(data)
        kit.insert_db()
        return Response({"message":"kit created succes"},status=status.HTTP_200_OK)
    
class ProductEntryView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        for key in request.data.get('product'):
            serializer = ProductSerializer(data =key)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            product = ProductModel.objects.get(name=data.get("name"))
            product.stock_product = product.stock_product + data.get("stock_product")
            product.save()
        return Response({"message":"Productos dado de alta"},status=status.HTTP_200_OK)
    