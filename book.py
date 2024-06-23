from models import Book
from storage import Storage

class BookManager:
    def __init__(self, storage_file='books.json'):
        self.storage_file = storage_file
        self.books = self.load_books()

    def load_books(self):
        """
        Load books from storage.
        """
        data = Storage.load_from_file(self.storage_file)
        return [Book(**book) for book in data]

    def save_books(self):
        """
        Save books to storage.
        """
        data = [book.__dict__ for book in self.books]
        Storage.save_to_file(data, self.storage_file)

    def add_book(self, title, author, isbn):
        if not title or not author or not isbn:
            raise ValueError("Title, author, and ISBN cannot be empty.")
        if not isinstance(isbn, str):
            raise ValueError("ISBN must be a string.")
        
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()
        print("Book added.")

    def list_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)

    def search_book(self, attribute, value):
        if attribute not in ['title', 'author', 'isbn']:
            raise ValueError("Invalid attribute for search.")
        
        results = [book for book in self.books if getattr(book, attribute) == value]
        return results

    def delete_book(self, isbn):
        if not isbn:
            raise ValueError("ISBN cannot be empty.")
        
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()
        print("Book deleted.")
