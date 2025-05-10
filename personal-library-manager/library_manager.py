import json  # For reading/writing JSON data to file
import os    # For checking if file exists

# Book class to represent a single book
class Book:
    def __init__(self, title, author, year, genre, read=False):
        self.title = title      # Title of the book
        self.author = author    # Author of the book
        self.year = year        # Year the book was published
        self.genre = genre      # Genre/category of the book
        self.read = read        # Boolean: True if the book has been read, False otherwise

    def to_dict(self):
        # Convert book object to dictionary format for JSON serialization
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'read': self.read
        }

    @staticmethod
    def from_dict(data):
        # Create a Book object from a dictionary (used when loading from JSON)
        return Book(**data)

# Library class to manage collection of books
class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename    # File to store the book list
        self.books = self.load_books()  # Load books from file or initialize an empty list

    def add_book(self, book):
        # Add a new book to the library
        self.books.append(book)
        print(f'✅ Book "{book.title}" added!')

    def remove_book(self, title):
        # Remove a book by title (case-insensitive match)
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'🗑️ Book "{title}" removed!')
                return
        print("❌ Book not found!")

    def search_books(self, keyword):
        # Search for books by title, author, or genre (case-insensitive)
        return [
            book for book in self.books
            if keyword.lower() in book.title.lower()
            or keyword.lower() in book.author.lower()
            or keyword.lower() in book.genre.lower()
        ]

    def display_books(self):
        # Print a list of all books in the library with their details
        if not self.books:
            print("📭 No books in the library.")
            return
        for i, book in enumerate(self.books, 1):
            status = "✅ Read" if book.read else "📖 Unread"
            print(f"{i}. {book.title} by {book.author} ({book.year}) - {book.genre} - {status}")

    def stats(self):
        # Display statistics: total books and how many are read
        total = len(self.books)
        read = sum(book.read for book in self.books)  # Count books marked as read
        print(f"📚 Total books: {total}")
        print(f"📘 Read: {read} ({(read / total * 100):.1f}%)" if total else "No data to show.")

    def save_books(self):
        # Save the current list of books to a JSON file
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def load_books(self):
        # Load books from the JSON file if it exists
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return [Book.from_dict(b) for b in json.load(f)]
        return []  # Return empty list if file doesn't exist

# Show the main menu options
def menu():
    print("\n📚 Library Manager")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Library Stats")
    print("6. Save and Exit")

# Ask user to input book details and return a Book object
def get_book_details():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    while True:
        try:
            year = int(input("Enter book year: "))
            break
        except ValueError:
            print("❌ Please enter a valid year.")
    genre = input("Enter book genre: ")
    read = input("Have you read this book? (y/n): ").strip().lower() == 'y'
    return Book(title, author, year, genre, read)

# Main function to run the interactive command-line app
def main():
    library = Library()  # Create a Library instance

    while True:
        menu()  # Show menu
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            library.add_book(get_book_details())  # Add new book
        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)  # Remove book by title
        elif choice == "3":
            keyword = input("Search by title/author/genre: ")
            results = library.search_books(keyword)  # Search for books
            if results:
                for book in results:
                    print(f"🔎 {book.title} by {book.author} ({book.year}) - {book.genre}")
            else:
                print("❌ No books found.")
        elif choice == "4":
            library.display_books()  # Show all books
        elif choice == "5":
            library.stats()  # Show stats
        elif choice == "6":
            library.save_books()  # Save to file and exit
            print("💾 Changes saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please choose between 1-6.")

# Entry point of the script
if __name__ == "__main__":
    main()
