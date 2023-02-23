from django.urls import path, include
from back.views import TestView

app_name = 'back'

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    
    ]