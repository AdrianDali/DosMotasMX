from django.urls import path, include
from back.views import TestView, ProductView, CategoryView, OrderView, KitView, ProductEntryView

app_name = 'back'

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('product/', ProductView.as_view(), name='product'),
    path('category/', CategoryView.as_view(), name='category'),
    path('order/', OrderView.as_view(), name='order'),
    path('kit/',KitView.as_view(), name= 'kit'),
    path('productEntry/' ,ProductEntryView.as_view(), name='productEntry'),
    ]