from django.db import models
from django import forms


# Create your models here.
#LOS USUARIOS QUE ESTARAN REGISTRADOS PARA HACER VENTAS 
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.email  
    
#LOS PRODUCTOS QUE ESTARAN REGISTRADOS POR SEPARADO         
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='shop/images', default="", null=True, blank=True)
    desc = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default="")
    sell_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

#LOS KITS QUE ESTARAN REGISTRADI A PARTRIR DE LOS PRODUCTOS 
class Kit(models.Model): 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='shop/images', default="", null= True, blank=True )
    desc = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default="")
    sell_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
#RELACION MUCHOS A MNUCHOS PARA CREAR EL KIT BASADO EN LOS PRODUCTOS 
class ProcuctKit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name + " " 
    
#ESTE MODELO MANTIENE UN REGISTRO DE LAS ENTRADAS QUE HAY DE PRODUCTOS 
class ProductEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_product = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=300, null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return self.product.name + " " + str(self.date)

#ESTE MODELO MANTIENE UN REGISTRO DE LAS ENTRADAS QUE HAY DE LOS KITS  
class KitEntry(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.kit.name + " " + str(self.quantity) + " " + str(self.date)
    
#ESTE MODELO MANTIENE UN REGISTRO DE LAS VENTAS QUE SE HACEN
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_quantity = models.IntegerField(default=0)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE, null=True, blank=True)
    kit_quantity = models.IntegerField(default=0)

    date = models.DateField()
    total = models.IntegerField(default=0)
    sold = models.BooleanField(default=False)


    def __str__(self):
        return  " " + str(self.kit.name) + " " + str(self.date)

#ESTE MODELO MANTIENE UN REGISTRO DE LAS CATEGORIAS DE LOS PRODUCTOS Y KITS
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop/images', default="", null=True, blank=True)

    def __str__(self):
        return self.name
