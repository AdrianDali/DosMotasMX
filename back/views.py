from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from back.serializers import CategorySerializer, ProductSerializer, OrderSerializer, KitSerializer,ProductEntrySerializer,GetKitProductSerializer
from back.classes import Category, Product, Order, Kit, Entry
from back.models import Product as ProductModel, Category as CategoryModel, Order as OrderModel, Kit as KitModel, ProductEntry as ProductEntryModel, ProductKit as ProductKitModel
import json
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login as auth_login, logout


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
        serializer = ProductEntrySerializer(data =request.data.get('entry'))
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print("######################DATA ENTRY######################")
        print(data)
        print(data.get("products")[0].get("name"))
        entry = Entry(data)
        print(entry.title)
        print(entry.total_amount)
        print(entry.date)
        print(entry.products)

        entry.insert_db()

        return Response({"message":"Productos dado de alta"},status=status.HTTP_200_OK)
    
class GetProductView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request): 
        products = ProductModel.objects.all()
        serializer_product = ProductSerializer(products,many=True)
        datos = serializer_product.data
        print(datos)

        return Response({"products":datos},status=status.HTTP_200_OK)
    
class GetCategoryView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request): 
        categories = CategoryModel.objects.all()
        serializer_category = CategorySerializer(categories,many=True)
        datos = serializer_category.data
        print(datos)

        return Response({"categories":datos},status=status.HTTP_200_OK)
    
class GetKitView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        kit = ProductKitModel.objects.all().select_related('kit').select_related('product')
        print("#######################")
        print(kit)
        serializer_kit = GetKitProductSerializer(kit,many=True)
        datos = serializer_kit.data
        print(datos)

        return Response({kit},status=status.HTTP_200_OK)


class GetOrderView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request): 
        orders = OrderModel.objects.all()
        serializer_order = OrderSerializer(orders,many=True)
        datos = serializer_order.data
        print(datos)

        return Response({"orders":datos},status=status.HTTP_200_OK)
    
class LoginView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 

        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        username =authenticate(username=username,password=password)

        if username is not None:
            auth_login(request,username)
            router = Token.objects.update_or_create(
                user = username
            )
            print("TOKEN")

            return Response({"message":"Login succes"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Login failed"},status=status.HTTP_200_OK)

class LogoutOperator(APIView):
    authentication_classes = (AllowAny,)

    def post(self,request):
        pass
