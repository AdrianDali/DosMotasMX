from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from back.serializers import CategorySerializer
from back.classes import Category

# Create your views here.
class TestView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        return Response({"message":"Hello World"},status=status.HTTP_200_OK)
    
class ProductView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 


        payload = request.data

        return Response({"message":"Hello World"},status=status.HTTP_200_OK)
    
class CategoryView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request): 
        for key in request.data:
            print(key)
            #probar aqui que no hay problema con el request.data 
            print(request.data.get(key))
            print(request.data.get('category')[1])
        serializer = CategorySerializer(data =request.data.get('category')[1])
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        print("la data")
        print(data.get("name"))

        category = Category(data.get("name"))

        category.insert_db()
        

        return Response({"message":"Category created succes"},status=status.HTTP_200_OK)
    