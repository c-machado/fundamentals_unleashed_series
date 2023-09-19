class DynamoProductRepo:
    def scan_table(self, filter=None, projection = [], index_name = None):
        print(f"running Dynamo scan on products table with parameters {filter}, {projection}, {index_name}")
        return [{"name": "t-shirt",    "stock": 500}, 
                {"name": "shoes",      "stock": 30}, 
                {"name": "sweatshirt", "stock": 300}]

class StockManager():
    def __init__(self, repo) -> None:
        self._repo = repo
        self.threshold = 50
        
    def check_products(self):
        products = self._repo.scan_table()
        print("Out of stock:")
        for product in products:
            if product['stock'] < self.threshold:
                print(f"- {product['name']}")

repo = DynamoProductRepo()
stockmanager = StockManager(repo=repo)
stockmanager.check_products()
