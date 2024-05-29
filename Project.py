# Mini-Project: Library Management System

import re
from book import Book, FictionBook, NonFictionBook
from user import User
from author import Author
from genre import Genre

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    # Methods for book operations
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        isbn = input("Enter the book ISBN: ")
        genre = input("Enter the book genre: ")
        publication_date = input("Enter the publication date: ")
        book = Book(title, author, isbn, genre, publication_date)
        self.books.append(book)
        print("Book added successfully.")

    def borrow_book(self):
        user_id = input("Enter your library ID: ")
        isbn = input("Enter the book ISBN: ")
        user = self.get_user_by_id(user_id)
        book = self.get_book_by_isbn(isbn)
        if user and book and book.get_status() == 'Available':
            user.borrow_book(book)
            book.set_status('Borrowed')
            print("Book borrowed successfully.")
        else:
            print("Cannot borrow book. Either the book is not available or user/book not found.")

    def return_book(self):
        user_id = input("Enter your library ID: ")
        isbn = input("Enter the book ISBN: ")
        user = self.get_user_by_id(user_id)
        book = self.get_book_by_isbn(isbn)
        if user and book:
            user.return_book(book)
            book.set_status('Available')
            print("Book returned successfully.")
        else:
            print("Cannot return book. Either the book is not found or user/book not found.")

    def search_book(self):
        isbn = input("Enter the book ISBN: ")
        book = self.get_book_by_isbn(isbn)
        if book:
            print(book)
        else:
            print("Book not found.")

    def display_all_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books available.")

    # Methods for user operations
    def add_user(self):
        name = input("Enter the user name: ")
        library_id = input("Enter the user library ID: ")
        user = User(name, library_id)
        self.users.append(user)
        print("User added successfully.")

    def view_user_details(self):
        user_id = input("Enter the user library ID: ")
        user = self.get_user_by_id(user_id)
        if user:
            print(user)
        else:
            print("User not found.")

    def display_all_users(self):
        if self.users:
            for user in self.users:
                print(user)
        else:
            print("No users available.")

    # Methods for author operations
    def add_author(self):
        name = input("Enter the author name: ")
        biography = input("Enter the author biography: ")
        author = Author(name, biography)
        self.authors.append(author)
        print("Author added successfully.")

    def view_author_details(self):
        name = input("Enter the author name: ")
        author = self.get_author_by_name(name)
        if author:
            print(author)
        else:
            print("Author not found.")

    def display_all_authors(self):
        if self.authors:
            for author in self.authors:
                print(author)
        else:
            print("No authors available.")

    # Methods for genre operations
    def add_genre(self):
        name = input("Enter the genre name: ")
        description = input("Enter the genre description: ")
        genre = Genre(name, description)
        self.genres.append(genre)
        print("Genre added successfully.")

    def view_genre_details(self):
        name = input("Enter the genre name: ")
        genre = self.get_genre_by_name(name)
        if genre:
            print(genre)
        else:
            print("Genre not found.")

    def display_all_genres(self):
        if self.genres:
            for genre in self.genres:
                print(genre)
        else:
            print("No genres available.")

    # Helper methods to get instances by identifiers
    def get_user_by_id(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        return None

    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                return book
        return None

    def get_author_by_name(self, name):
        for author in self.authors:
            if author.get_name() == name:
                return author
        return None

    def get_genre_by_name(self, name):
        for genre in self.genres:
            if genre.get_name() == name:
                return genre
        return None

    # Menus for user interaction
    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                self.genre_operations()
            elif choice == '5':
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def genre_operations(self):
        while True:
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_genre()
            elif choice == '2':
                self.view_genre_details()
            elif choice == '3':
                self.display_all_genres()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.main_menu()
