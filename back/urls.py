from django.urls import path, include
from back.views import TestView, ProductView, CategoryView, OrderView, KitView, ProductEntryView, GetProductView, GetCategoryView, GetOrderView, GetKitView

app_name = 'back'

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('product/', ProductView.as_view(), name='product'),
    path('category/', CategoryView.as_view(), name='category'),
    path('order/', OrderView.as_view(), name='order'),
    path('kit/',KitView.as_view(), name= 'kit'),
    path('productEntry/' ,ProductEntryView.as_view(), name='productEntry'),
    path('getProducts/',GetProductView.as_view(), name='getProducts'),
    path('getCategories/',GetCategoryView.as_view(), name='getCategories'),
    #Aun no funcionan 
    path('getOrders/',GetOrderView.as_view(), name='getOrders'),
    path('getKits/',GetKitView.as_view(), name='getKits'),

    ]