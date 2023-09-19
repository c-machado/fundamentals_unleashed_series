# ############ static duck typing with typing.Protocol #################
from typing import List, Protocol, runtime_checkable

@runtime_checkable   # Required for 'isinstance' checks to work with Protocols at runtime.
class ProductRepo(Protocol):
    def get_all_products(self) -> List:
        '''should retrieve all the products from the database'''
        raise NotImplementedError
    def get_shoes(self) -> List:
        '''should retrieve all the shoes from the database'''
        raise NotImplementedError

class SQLProductRepo:
    def get_all_products(self) -> List:
        print("running query: SELECT * FROM products")
        return [{"name": "t-shirt",    "stock": 500}, 
                {"name": "shoes",      "stock": 30}, 
                {"name": "sweatshirt", "stock": 300}]

class DynamoProductRepo:
    def get_all_products(self) -> List:
        print("running Dynamo scan on products table")
        return [{"name": "t-shirt",    "stock": 500}, 
                {"name": "shoes",      "stock": 30}, 
                {"name": "sweatshirt", "stock": 300}]

class StockManager():
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