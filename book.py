class Book:
    def __init__(self, title, author, isbn, genre, publication_date, status='Available'):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self.__status = status

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}, Publication Date: {self.__publication_date}, Status: {self.__status}"


class FictionBook(Book):
    def __init__(self, title, author, isbn, genre, publication_date, status='Available', sub_genre='General Fiction'):
        super().__init__(title, author, isbn, genre, publication_date, status)
        self.__sub_genre = sub_genre

    def get_sub_genre(self):
        return self.__sub_genre

    def set_sub_genre(self, sub_genre):
        self.__sub_genre = sub_genre

    def __str__(self):
        return super().__str__() + f", Sub-genre: {self.__sub_genre}"


class NonFictionBook(Book):
    def __init__(self, title, author, isbn, genre, publication_date, status='Available', field='General'):
        super().__init__(title, author, isbn, genre, publication_date, status)
        self.__field = field

    def get_field(self):
        return self.__field

    def set_field(self, field):
        self.__field = field

    def __str__(self):
        return super().__str__() + f", Field: {self.__field}"
