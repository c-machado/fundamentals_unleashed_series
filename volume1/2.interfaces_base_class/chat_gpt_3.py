class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_title(self):
        return f"Title: {self.title}"

    def get_author(self):
        return f"Author: {self.author}"

    def get_price(self):
        return f"Price: {self.price:.1f}"

    def __str__(self):
        return f"{self.get_title()}\n{self.get_author()}\n{self.get_price()}"


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)
        if self.price <= 0:
            raise ValueError("Price not valid")

    def get_price(self):
        return f"Price: {self.price * 1.3:.1f}"


# Example usage:
try:
    book = Book("Sample Book", "John Doe", 25.99)
    print("Regular Book:")
    print(book)

    golden_book = GoldenEditionBook("Special Book", "Jane Smith", 19.99)
    print("\nGolden Edition Book:")
    print(golden_book)

    # Uncomment the line below to see the exception message for an invalid price.
    invalid_book = GoldenEditionBook("Invalid Book", "Invalid Author", -10)

except ValueError as e:
    print(f"Error: {e}")