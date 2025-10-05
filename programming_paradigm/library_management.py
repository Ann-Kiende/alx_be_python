# library_management.py

class Book:
    """A simple Book class with title, author, and checkout status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out if it’s available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """A Library class that manages a collection of Book objects."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """Mark a book as returned by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """Print all available books in 'Title by Author' format."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
