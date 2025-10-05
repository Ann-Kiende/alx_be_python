# library_management.py

from typing import List, Optional

class Book:
    """
    A Book represents a single book in the library.

    Public attributes:
      - title (str)
      - author (str)

    Private attribute:
      - _is_checked_out (bool): True if the book is checked out, False otherwise
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> bool:
        """
        Mark the book as checked out.
        Returns True if the checkout succeeded, False if the book was already checked out.
        """
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """
        Mark the book as returned (available).
        Returns True if the return succeeded, False if the book was not checked out.
        """
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, checked_out={self._is_checked_out})"


class Library:
    """
    A Library manages a collection of Book instances.

    Private attribute:
      - _books (List[Book])
    """
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a Book instance to the library collection."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance")
        self._books.append(book)

    def _find_book_by_title(self, title: str) -> Optional[Book]:
        """Return the first Book with a matching title (exact match) or None if not found."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title: str) -> bool:
        """
        Attempt to check out a book by title.
        Returns True if checkout succeeded, False otherwise (not found or already checked out).
        """
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.check_out()

    def return_book(self, title: str) -> bool:
        """
        Attempt to return a book by title.
        Returns True if return succeeded, False otherwise (not found or not checked out).
        """
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.return_book()

    def list_available_books(self) -> None:
        """
        Print all available books (not checked out) in the format:
          Title by Author
        If no books available, prints nothing.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
