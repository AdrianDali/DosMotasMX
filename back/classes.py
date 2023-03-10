from back.models import ProductKit as ProductkitModel, OrderKit as OrderKitModel ,OrderProduct as OrderProductModel, Product as ProductModel, Category as CategoryModel, Order as OrderModel, User as UserModel, Kit as KitModel
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
            
class Order:
    def __init__ (self, data) -> None:
        self.user_name = data.get("user_name")
        self.title = data.get("title")
        self.date = data.get("date")
        self.total = data.get("total")
        self.sold = data.get("sold")
        self.products_sold = data.get("products")
        self.kits_sold = data.get("kits")
        print("###########################sadasd")
        print(self.kits_sold)
        print(self.products_sold)


        self.db_instance: ProductModel | None = None

    def insert_db(self):
        print("product sold")
        print(self.products_sold[0].get("name"))

        if OrderModel.objects.filter(title=self.title).exists(): 
            print("Producto ya existe")
            pass
        else:
            try:
                self.db_instance = OrderModel.objects.create(
                    user= UserModel.objects.get(name=self.user_name),
                    title=self.title,
                    date=self.date,
                    total=self.total,
                    sold=self.sold
                )
            except Exception as e:
                print(e)
                raise Exception('Error inserting product in database')
            


        productos = ProductModel.objects.filter(name=self.products_sold[0].get("name"))
        print(type(productos[0]))
        if productos.exists():



            print("Producto ya exsssssssssssssssssssssssiste")
            OrderProduct = OrderProductModel.objects.create(
                order=self.db_instance,
                product=productos[0],
                quantity=1,
                comment="hola")
            print("se creo con exito")


        kits = KitModel.objects.filter(name=self.kits_sold[0].get("name"))
        if kits.exists():
            print("Kit ya existe")
            OrderKit = OrderKitModel.objects.create(
                order = self.db_instance, 
                kit = kits[0],
                quantity = 1,
                comment = "hola"
            )


        
class Kit:
    def __init__(self,data) -> None:
        self.name = data.get("name")
        self.price = data.get("price")
        self.stock_kit = data.get("stock_kit")
        self.desc = data.get("desc")
        self.category = data.get("category")
        self.sell_price = data.get("sell_price")
        self.products = data.get("products")

        self.db_instance: KitModel | None = None

    def insert_db(self):
        if KitModel.objects.filter(name=self.name).exists(): 
            print("Producto ya existe")
            pass
        else:
            try:
                self.db_instance = KitModel.objects.create(
                    name=self.name,
                    price=self.price,
                    stock_kit=self.stock_kit,
                    desc=self.desc,
                    category=CategoryModel.objects.get(name=self.category),
                    sell_price=self.sell_price
                )                    

            except Exception as e:
                print(e)
                raise Exception('Error inserting product in database')

            try: 
                productos = ProductModel.objects.filter(name=self.products[0].get("name"))
                print(productos[0])
                if productos.exists():
                    pr = ProductkitModel.objects.create(
                        kit=self.db_instance,
                        product=productos[0],
                    )
                    print("Producto ya existe")
            except Exception as e:
                print(e)
                raise Exception('Error inserting product in database')
        
    