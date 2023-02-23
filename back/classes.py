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
        
    