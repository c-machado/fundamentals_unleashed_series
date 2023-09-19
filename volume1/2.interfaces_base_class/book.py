class Book:
    def __init__(self, title, author, price) -> None:
        self.title=title
        self.author=author
        self.price=price
       
        if self.author[0].isdigit():
            raise ValueError(f'author not valid')
        
        if len(self.title)<3:
            raise ValueError(f'Title not valid!')
        
        if self.price<=0:
            raise ValueError(f'Price not valid!')
        
    def __str__(self):
        return f"{self.title} ({self.author} just for: {self.price})"


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price=price*0.3)

    def __str__(self):
        return f"{self.title} ({self.author} just for: {self.price})"



if __name__ == "__main__":
    book1 = Book('el olvido que seremos', 'hector', 20000)
    print(book1)
    book2 = GoldenEditionBook('el olvido que seremos', 'hector', 20000)
    print(book2)    


