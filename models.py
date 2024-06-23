class Book:
    def __init__(self, title, author, isbn):
        """
        Initialize a new book instance.

        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN number of the book
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class User:
    def __init__(self, name, user_id):
        """
        Initialize a new user instance.

        :param name: Name of the user
        :param user_id: User ID
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"
