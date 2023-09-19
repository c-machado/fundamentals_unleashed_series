# #################### Traditional Duck Typing ######################

class SQLProductRepo:
    # updated the class's public interface with database-agnostic equivalents
    def get_all_products(self):
        print("running query: SELECT * FROM products")
        return [{"name": "t-shirt",    "stock": 500}, 
                {"name": "shoes",      "stock": 30}, 
                {"name": "sweatshirt", "stock": 300}]

class DynamoProductRepo:
    # updated the class's public interface with database-agnostic equivalents
    def get_all_products(self):
        print(f"running Dynamo scan on products table")
        return [{"name": "t-shirt",    "stock": 500}, 
                {"name": "shoes",      "stock": 30}, 
                {"name": "sweatshirt", "stock": 300}]

class StockManager():
    def __init__(self, repo) -> None:
        self._repo = repo
        self.threshold = 50
        
    def check_products(self):
        # update the invocation with the new database-agnostic interface
        products = self._repo.get_all_products()
        print("Out of stock:")
        for product in products:
            if product['stock'] < self.threshold:
                print(f"- {product['name']}")

repo = SQLProductRepo()
stockmanager = StockManager(repo=repo)
stockmanager.check_products()