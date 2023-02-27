from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from back.serializers import CategorySerializer, ProductSerializer
from back.classes import Category, Product

# Create your views here.
class TestView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        return Response({"message":"Hello World"},status=status.HTTP_200_OK)
    
class ProductView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        for product in request.data.get('product'):
            print(product)

            serializer = ProductSerializer(data =product)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            product = Product(data.get("name"),data.get("price"),data.get("stock_product"),data.get("desc"),data.get("category"),data.get("sell"))
            product.insert_db()


        return Response({"message":"Hello World"},status=status.HTTP_200_OK)
    
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
    