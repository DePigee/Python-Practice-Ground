class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        keep_books = []
        for b in self.books:
            if(b.title != book.title or b.author != book.author):
                keep_books.append(b)
        self.books = keep_books
       
    def search_books(self, search_string):
        matched_books = []

        for book in self.books:
            if(search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower()):
                 matched_books.append(book)
        return matched_books
        

book1 = Book("Stan Lee", "Avengers Endgame")
book2 = Book("Stan Lee", "Avengers Age of Ultron")
book3 = Book("Stan Lee", "Ironman")
book4 = Book("Stan Lee", "Spiderman - Homecoming")
book5 = Book("Stan Lee", "Black Panther")

Avengers = Library("Stark industries")

Avengers.add_book(book1)
Avengers.add_book(book2)
Avengers.add_book(book3)
Avengers.add_book(book4)
Avengers.add_book(book5)

search_query = Avengers.search_books("Avengers")
search_query1 = Avengers.search_books("Spiderman")

for book in search_query:
    print(f"{book.title} and {book.author}")

for book in search_query1:
    print(f"{book.title} and {book.author}")




