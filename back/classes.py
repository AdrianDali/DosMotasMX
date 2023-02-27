from back.models import Product, Category as CategoryModel

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
    def __init__(self, name, price, stock_product, desc, category, sell):
        self.name = name
        self.price = int(price)
        self.stock_product = int(stock_product)
        self.desc = desc
        self.category = category
        self.sell = int(sell)

        self.db_instance: Product | None = None

    def insert_db(self):
        if not self.db_instance is None: 
            raise Exception('Product already in database')
        try:
            self.db_instance = Product.objects.create(
                name=self.name,
                price=self.price,
                stock_product=self.stock_product,
                desc=self.desc,
                category=self.category,
                sell=self.sell
            )
        except Exception as e:
            raise Exception('Error inserting product in database')

        
    