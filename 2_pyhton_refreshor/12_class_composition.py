class BookShelf:
    def __init__(self,quantity):
        self.quantity=quantity
    def __str__(self):
        return f"BookShelf with {self.quantity} books"
class Book(BookShelf):
    def __init__(self,name,quantity):
        self.name=name
        super().__init__(quantity)
    def __str__(self):
        return f"Book: {self.name}"
book = Book("Harry Potter",100)
print(book)

# The above example is -> Every Book is a BookShelf
# Another good way is composition
#     COMPOSITION -> A Bookshelf has many books

class BookShelf2:
    def __init__(self,*books):
        self.books = books
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."
class Book2():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Book {self.name}"
book = Book2("Harry Potter")
print(book)


# TypeHinting
def add(a:int,b:int,c:int) -> float:
    return a+b+c
print(add(1,2,3))