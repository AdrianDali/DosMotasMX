from django.urls import path, include
from back.views import TestView, ProductView, CategoryView

app_name = 'back'

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('product/', ProductView.as_view(), name='product'),
    path('category/', CategoryView.as_view(), name='category')
    ]