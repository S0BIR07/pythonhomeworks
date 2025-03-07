class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title: str,author: str):
        self.title=title
        self.author = author
        self.is_borrowed=False
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Is borrowed: {self.is_borrowed}"

class Member:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book:Book):
        if len(self.borrowed_books)>=3: #number of borrowed books cannot be more than 3
            raise MemberLimitExceededException("Already reached the limit of 3 books!")
        elif book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed!")
        else: 
            self.borrowed_books.append(book)
            print("Book is borrowed successfully!")
            book.is_borrowed=True
    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise BookNotFoundException("You have not borrowed this book yet!")
        else:
            self.borrowed_books.remove(book)
            print("Book is returned!")
            book.is_borrowed = False
    def __str__(self):
        return f"Name: {self.name}, Borrowed books: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_member(self, name:str):
        self.members.append(Member(name))
    def add_book(self, title: str, author: str):
        self.books.append(Book(title=title, author=author))
    def borrow(self, name: str, title: str):
        member = next((m for m in self.members if m.name==name),None)
        if not member:
            raise ValueError(f"Member {name} is not found!")
        book = next((m for m in self.books if title==m.title),None)
        if not book:
            raise BookNotFoundException("Book is not found!")
        member.borrow_book(book)
    def return_book(self, name: str, title: str):
        member = next((m for m in self.members if m.name==name),None)
        if not member:
            raise ValueError(f"Member {name} is not found!")
        book = next((m for m in self.books if title==m.title), None)
        if not book:
            raise BookNotFoundException("Book is not found!")
        member.return_book(book)
        print("Book is returned successfully!")
        book.is_borrowed = False
        
def main():
    library = Library()

    book5 = Book(title="Patriot", author="Alexei Navalny")

    library.add_book(title="Idiot", author="Fyodor Dostoevsky")
    library.add_book(title="Harry Potter", author="Joanne Rowling")
    library.add_book(title="Romeo and Juliet", author="William Shakespeare")
    library.add_book(title="Atomic Habits", author="James Clear")

    library.add_member(name="Akbar")
    library.add_member(name="Shaxzod")
    library.add_member(name="Asilbek")
    library.add_member(name="Bexruz")

    library.borrow("Akbar", "Idiot") # Test for simple borrowing
    library.borrow("Akbar", "Harry Potter")
    library.borrow("Akbar", "Atomic Habits")
#    library.borrow("Akbar", "Romeo and Juliet") # Test for member limit exceeded exception
#    library.return_book("Shaxzod", "Idiot") # Test for book not found exception
#    library.borrow("Asilbek", "Idiot") # Test for book already borrowed exception
    library.borrow("Akobir", "Romeo and Juliet") # Test for member not found error
if __name__ == "__main__":
    main()