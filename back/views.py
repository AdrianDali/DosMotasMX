from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from back.serializers import CategorySerializer, ProductSerializer, OrderSerializer, KitSerializer,ProductEntrySerializer,GetKitProductSerializer
from back.classes import Category, Product, Order, Kit, Entry
from back.models import Product as ProductModel, Category as CategoryModel, Order as OrderModel, Kit as KitModel, ProductEntry as ProductEntryModel, ProductKit as ProductKitModel ,OrderProduct as OrderProductModel, OrderKit as OrderKitModel, Entry as EntryModel
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
        aux = []
        kits = KitModel.objects.all()

        kits_products = ProductKitModel.objects.filter(kit = KitModel.objects.get( name = kits[0].name)).select_related('product').values("product__name","product__price")        




        print(kits_products)    

        for i in kits:
            print("#################################")
            print(i)
            print("s#################################")


            a = {}
            a.update({"name":i.name})
            a.update({"price":i.price})
            a.update({"products":kits_products})
            aux.append(a)
            

        return Response({"kits": aux},status=status.HTTP_200_OK)


class GetOrderView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request): 
        aux = []
        orders = OrderModel.objects.all().values("user__username", "title","date" , "total", "sold")
        order_product = OrderProductModel.objects.filter(order = OrderModel.objects.get( title = orders[0].get("title"))).select_related('product').values("product__name","product__price")
        order_kit = OrderKitModel.objects.filter(order  = OrderModel.objects.get( title = orders[0].get("title"))).select_related('kit').values("kit__name","kit__price")

        for i in orders:
            a = {}
            a.update(i)
            a.update({"products":order_product})
            a.update({"kits":order_kit})
            aux.append(a)
        
        return Response({"orders":aux},status=status.HTTP_200_OK)
    
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


class FilterProductView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        aux = []
        products = ProductModel.objects.filter(name = request.data.get("product")).values("name","price","category__name")
        print(products)
        for i in products:
            a = {}
            a.update(i)
            aux.append(a)
            
        return Response({"product": aux},status=status.HTTP_200_OK)
    
class DeleteCategory(APIView):
    permission_classes = (AllowAny,)
    def delete(self,request):

        data = request.data.get("category")
        category =CategoryModel.objects.get(name = data) 
        category.delete()
        return Response({"category" : "categoria borrada"}, status= status.HTTP_200_OK)


class DeleteProduct(APIView):
    permission_classes = (AllowAny,)
    def delete(self,request):
        data = request.data.get("product")
        product = ProductModel.objects.get(name = data)
        product.delete()
        return Response({"product": "producto borrado"}, status= status.HTTP_200_OK)
    
class DeleteKit(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request): 
        data = request.data.get("kit")
        kit = KitModel.objects.get(name = data)
        kit.delete()
        return Response({"kit": "kit borrador"}, status=status.HTTP_201_CREATED)

class DeleteOrder(APIView):
    permission_classes = (AllowAny,)
    def delete(self,request):
        data = request.data.get("order")
        order = OrderModel.objects.get(name = data)
        order.delete()
        return Response({"order": "orden borrada"}, status= status.HTTP_200_OK)
    
class EditCategory(APIView):
    permission_classes = (AllowAny,)
    def put(self,request):
        #data = request.data.get("category")
        category = CategoryModel.objects.get(name = request.data.get("name"))
        category.name = request.data.get("new_name")
        category.save()
        return Response({"category": "categoria editada"}, status= status.HTTP_200_OK)

class EditProduct(APIView):
    permission_classes = (AllowAny,)
    def put(self,request):
        data = request.data.get("product")
        product = ProductModel.objects.get(name = data.get("name"))
        product.name = data.get("new_name")
        product.price = data.get("new_price")
        product.desc = data.get("new_desc")
        product.category = CategoryModel.objects.get(name = data.get("new_category"))
        product.sell_price = data.get("new_sell_price")
        
        product.save()
        return Response({"product": "producto editado"}, status= status.HTTP_200_OK)
    
class EditKit(APIView):
    permission_classes = (AllowAny,)
    def put(self,request):
        data = request.data.get("kit")
        kit = KitModel.objects.get(name = data.get("name"))
        kit.name = data.get("new_name")
        kit.price = data.get("new_price")
        kit.save()
        return Response({"kit": "kit editado"}, status= status.HTTP_200_OK)

class EditOrder(APIView):
    permission_classes = (AllowAny,)
    def put(self,request):
        data = request.data.get("order")
        order = OrderModel.objects.get(name = data.get("name"))
        order.name = data.get("new_name")
        order.save()
        return Response({"order": "orden editada"}, status= status.HTTP_200_OK)

