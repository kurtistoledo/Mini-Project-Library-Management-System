class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, library_id):
        self.__library_id = library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        self.__borrowed_books.remove(book)

    def __str__(self):
        borrowed_books_titles = [book.get_title() for book in self.__borrowed_books]
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {', '.join(borrowed_books_titles)}"
