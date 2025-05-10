class Book:
    # Class variable to track total number of books
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment the total books count when a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        """Class method to increment the total books count"""
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        """Class method to get the total number of books"""
        return cls.total_books

# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Print the total number of books
print(f"Total books in library: {Book.get_total_books()}")  # Output: 3

# Access class variable directly
print(f"Total books (direct access): {Book.total_books}")   # Output: 3

"""
Explanation:
1. total_books is a class variable shared by all instances
2. @classmethod decorator marks methods that work with the class
3. increment_book_count() is called in __init__ to update the count
4. Class methods can be called on the class itself (Book.method())
5. Class variables can be accessed through the class (Book.variable)
"""
