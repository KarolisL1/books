from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.favorite import Favorite

@app.route('/favorites/<int:author_id>/insert_author', methods=["POST"])
def create_favorite(author_id):
    data = {
        'author_id': author_id,
        'book_id': request.form['book_id']
    }
    Favorite.save_favorite(data)
    return redirect(f'/authors/{author_id}')


@app.route('/favorites/<int:book_id>/insert_book', methods=["POST"])
def create_favorite2(book_id):
    data = {
        'book_id': book_id,
        'author_id': request.form['author_id']
    }
    Favorite.save_favorite(data)
    return redirect(f'/books/{book_id}')