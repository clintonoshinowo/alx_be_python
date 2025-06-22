class Book:
    """
    A class to represent a book, demonstrating Python magic methods.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """

    def __init__(self, title, author, year):
        """
        Constructor method (__init__).
        Initializes a new Book instance with provided title, author, and year.
        This method is automatically called when a new object is created (e.g., Book("Title", "Author", 2023)).
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method (__del__).
        Called automatically when the object is about to be destroyed or garbage-collected.
        Prints a message indicating the book being deleted.
        Note: The exact timing of __del__ calls can be unpredictable due to garbage collection.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation method (__str__).
        Returns a user-friendly, informal string representation of the object.
        This method is called by functions like print() and str().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation method (__repr__).
        Returns an unambiguous, developer-friendly string representation of the object.
        Ideally, this string should be a valid Python expression that could recreate the object.
        This method is called by repr() and in interactive shells.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
