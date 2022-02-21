from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book, author

class Favorite():
    def __init__(self, data):
        self.id = data['id']
        self.book_id = data['book_id']
        self.author_id = data['author_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_favorite(cls, data ):
        query = "INSERT INTO favorites ( book_id , author_id) VALUES ( %(book_id)s , %(author_id)s );"
        # data is a dictionary that will be passed into the save method from server.py

        return connectToMySQL('books_schema').query_db( query, data )