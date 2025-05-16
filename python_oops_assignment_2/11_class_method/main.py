# # 11. Class Methods
# # Assignment:
# # Create a class Book with a class variable total_books. 
# # Add a class method increment_book_count() to increase the count when a new book is added.

# # Create an instance method display_book_count() to display the total number of books.

# class Book:
#     total_books = 0  # Class variable

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.increment_book_count()  # Call class method when a book is created

#     @classmethod
#     def increment_book_count(cls):
#         cls.total_books += 1

# # Example usage
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")

# print(f"Total books: {Book.total_books}")




# Print with author name
class Book:
    total_books = 0  # Class variable to keep track of all books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def print_author(self):
        print(f"Author of '{self.title}' is {self.author}")

# Example usage
book1 = Book("Tafhim ul Quran", "Moulana Maududi")
book2 = Book("Biyan ul Quran", "Dr Israr Ahmed")
# Print book titles

# Print author names
book1.print_author()
book2.print_author()

# Print total number of books
print(f"Total books: {Book.total_books}")

