from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book():
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def all_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of friends
        books = []
        # Iterate over the db results and create instances of friends with cls.
        for book in results:
            books.append( cls(book) )
        return books

    @classmethod
    def save_book(cls, data ):
        query = "INSERT INTO books ( title , num_of_pages,) VALUES ( %(book_title)s , %(num_of_pages)s );"

        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_one_book(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query, data )
        return cls(results[0])

    @classmethod
    def get_book_with_authors( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db( query , data )
        books = cls( results[0] )
        for row_from_db in results:
            author_data = {
                "id" : row_from_db["authors.id"],
                "name" : row_from_db["name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            books.authors.append( author.Author( author_data ) )
        return books