from django.urls import path, include
from back.views import TestView, ProductView, CategoryView, OrderView, KitView, ProductEntryView, GetProductView, GetCategoryView, GetOrderView, GetKitView, LoginView, FilterProductView, DeleteCategory, DeleteKit , DeleteOrder, DeleteProduct, EditCategory, EditKit, EditOrder, EditProduct


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
    path('login/',LoginView.as_view(), name='login'),
    path('getKits/',GetKitView.as_view(), name='getKits'),
    path('filterProducts/',FilterProductView.as_view(), name='filterProducts'),
    path('deleteCategory/',DeleteCategory.as_view(), name='deleteCategory'),
    path('deleteProduct/',DeleteProduct.as_view(), name='deleteProduct'),
    path('deleteKit/',DeleteKit.as_view(), name='deleteKit'),
    path('deleteOrder/',DeleteOrder.as_view(), name='deleteOrder'),
    path('editCategory/',EditCategory.as_view(), name='editCategory'),
    path('editProduct/',EditProduct.as_view(), name='editProduct'),
    path('editKit/',EditKit.as_view(), name='editKit'),
    path('editOrder/',EditOrder.as_view(), name='editOrder'),



    #Aun no funcionan 
    path('getOrders/',GetOrderView.as_view(), name='getOrders'),
    


    ]