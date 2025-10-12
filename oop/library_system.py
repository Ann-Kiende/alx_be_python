# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a readable string representation for a Book."""
        return f"Book: {self.title} by {self.author}"


# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        """Return a readable string representation for an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a readable string representation for a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition Class: Library
class Library:
    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
