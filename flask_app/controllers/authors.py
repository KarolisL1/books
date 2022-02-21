from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect("/authors")

@app.route('/create_author', methods=["POST"])
def create_author():
    Author.save_author(request.form)
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.all_authors()
    return render_template('authors.html', authors=authors)

@app.route('/authors/<int:id>')
def single_author(id):
    data = {'id': id}
    author = Author.get_author_with_books(data)
    all_books = Book.all_books()
    return render_template('authors_show.html', author=author, all_books=all_books)