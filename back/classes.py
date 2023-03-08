from back.models import Product as ProductModel, Category as CategoryModel
from rest_framework import status 
from rest_framework.response import Response

class Category: 
    def __init__(self,name): 
        self.name = name 

        self.db_instance: CategoryModel | None = None

    def insert_db(self):

        if not self.db_instance is None: 
            raise Exception('Category already in database')
        try:
            self.db_instance = CategoryModel.objects.create(name=self.name)
        except Exception as e:
            raise Exception('Error inserting category in database')
        

class Product:
    def __init__(self, data ) -> None:

        self.name = data.get("name")
        self.price = int(data.get("price"))
        self.stock_product = int(data.get("stock_product"))
        self.desc =  data.get("desc")
        self.category = Category(data.get("category")) 
        self.sell = data.get("sell_price")

        self.db_instance: ProductModel | None = None


    def insert_db(self):

        

        if ProductModel.objects.filter(name=self.name).exists(): 
            print("Producto ya existe")
            pass
        else:
            try:
                self.db_instance = ProductModel.objects.create(
                    name=self.name,
                    price=self.price,
                    stock_product=self.stock_product,
                    desc=self.desc,
                    category=CategoryModel.objects.get(name=self.category.name),
                    sell_price=self.sell
                )
            except Exception as e:
                print(e)
                raise Exception('Error inserting product in database')
        

        
    