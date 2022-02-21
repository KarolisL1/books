from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def all_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of friends
        authors = []
        # Iterate over the db results and create instances of friends with cls.
        for author in results:
            authors.append( cls(author) )
        return authors

    @classmethod
    def save_author(cls, data ):
        query = "INSERT INTO authors ( name , created_at, updated_at ) VALUES ( %(author_name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py

        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query, data )
        return cls(results[0])

    @classmethod
    def get_author_with_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        authors = cls( results[0] )
        for row_from_db in results:
            # Now we parse the topping data to make instances of toppings and add them into our list.
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            authors.books.append( book.Book( book_data ) )
        return authors