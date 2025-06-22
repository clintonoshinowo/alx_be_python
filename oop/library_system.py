class Book:
    """
    A base class representing a generic book.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book.
        This method is overridden in derived classes to provide specific details.
        """
        return f"Book: {self.title} by {self.author}"

# Derived Class: EBook
# Represents an electronic book, inheriting from Book.
class EBook(Book):
    """
    A derived class representing an electronic book.
    Inherits from Book and adds a file_size attribute.
    Attributes:
        title (str): The title of the e-book.
        author (str): The author of the e-book.
        file_size (int): The size of the e-book file in KB.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes a new EBook instance.
        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook, including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class: PrintBook
# Represents a physical print book, inheriting from Book.
class PrintBook(Book):
    """
    A derived class representing a physical print book.
    Inherits from Book and adds a page_count attribute.
    Attributes:
        title (str): The title of the print book.
        author (str): The author of the print book.
        page_count (int): The number of pages in the print book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a new PrintBook instance.
        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook, including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition Class: Library
# Manages a collection of various book types using composition.
class Library:
    """
    A class representing a library that manages a collection of books.
    Demonstrates composition by holding instances of Book, EBook, and PrintBook.
    Attributes:
        books (list): A list to store various book instances.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.
        Args:
            book (Book): An instance of Book or its derived classes.
        """
        if isinstance(book, Book):
            self.books.append(book)
            # Removed the print statement here
        else:
            # You might want to handle this error differently if it's unexpected
            # but for exact output, we'll keep it silent or remove it.
            pass # Removed the print statement: print("Error: Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
        if not self.books:
            # Removed the print statement here, as expected output shows nothing for empty.
            return

        # Removed the header and footer print statements to match expected output exactly
        # print("\n--- Books in the Library ---")
        for book in self.books:
            print(book)
        # print("----------------------------")


