from book_class import Book

def main():
    # Creating an instance of Book
    # This will automatically call the __init__ method defined in book_class.py
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    # The print() function will implicitly call my_book.__str__()
    print(my_book)

    # Demonstrating the __repr__ method
    # The repr() built-in function explicitly calls my_book.__repr__()
    print(repr(my_book))

    # Deleting a book instance to trigger __del__
    # The __del__ method is called when the object's reference count drops to zero,
    # which often happens immediately after 'del my_book' in simple scripts.
    del my_book

if __name__ == "__main__":
    main()
