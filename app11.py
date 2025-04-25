#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-11-Class Methods
#Create a class Book with a class variable total_books. Add a class method increment_book_count()
#to increase the count when a new book is added.

class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Automatically increment when a book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Accessing and modifying class variable

    @classmethod
    def display_total_books(cls):
        print(f"Total books: {cls.total_books}")

# Creating book objects
book1 = Book("Python Basics")
book2 = Book("Advanced Python")
book3 = Book("English")
book4 = Book("Mathematics")
book5 = Book("Science")

# Display total books
Book.display_total_books() #Total books:5
