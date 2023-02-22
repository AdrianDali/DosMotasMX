from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def _str_(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='shop/images', default="")
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    sell_price = models.IntegerField(default=0)

    def _str_(self):
        return self.name


class Kit(models.Model): 
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='shop/images', default="")
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    sell_price = models.IntegerField(default=0)

    def _str_(self):
        return self.name
    
class ProcuctKit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)

    def _str_(self):
        return self.product.name + " " + self.kit.name
    
class ProductEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()

    def _str_(self):
        return self.product.name + " " + str(self.quantity) + " " + str(self.date)
    
class KitEntry(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()

    def _str_(self):
        return self.kit.name + " " + str(self.quantity) + " " + str(self.date)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_quantity = models.IntegerField(default=0)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    kit_quantity = models.IntegerField(default=0)

    date = models.DateField()
    total = models.IntegerField(default=0)
    sold = models.BooleanField(default=False)


    def _str_(self):
        return self.user.name + " " + self.product.name + " " + self.kit.name + " " + str(self.date)


