# ############################ Custom ABCs #############################
from abc import ABC, abstractmethod
from typing import List

# we can also make ProductRepo an ABC by using metaclass=ABCMeta 
class ProductRepo(ABC):
    @abstractmethod   #must use this annotation to declare a method abstract
    def get_all_products(self) -> List:
        '''should retrieve all the products from the database'''
        pass

class SQLProductRepo(ProductRepo):
    # pass
    def get_all_products(self) -> List:
        print("running query: SELECT * FROM products")
        return [{"name": "t-shirt",    "stock": 500}, 
                {"name": "shoes",      "stock": 30}, 
                {"name": "sweatshirt", "stock": 300}]
        
class DynamoProductRepo(ProductRepo):
    def get_all_products(self) -> List:
        print(f"running Dynamo scan on products table")
        return [{"name": "t-shirt",    "stock": 500}, 
                {"name": "shoes",      "stock": 30}, 
                {"name": "sweatshirt", "stock": 300}]

class StockManager:
    def __init__(self, repo: ProductRepo) -> None:
        self._repo = repo
        self.threshold = 50
        
    def check_products(self) -> None:
        products = self._repo.get_all_products()
        print("Out of stock:")
        for product in products:
            if product['stock'] < self.threshold:
                print(f"- {product['name']}")

repo = SQLProductRepo()
stockmanager = StockManager(repo=repo)
stockmanager.check_products()