from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/b')
def new_book():
    return redirect("/books")

@app.route('/books')
def books():
    books = Book.all_books()
    return render_template('books.html', books=books)

@app.route('/create_book', methods=["POST"])
def create_book():
    Book.save_book(request.form)
    return redirect('/books')

@app.route('/books/<int:id>')
def single_book(id):
    data = {'id': id}
    book = Book.get_book_with_authors(data)
    all_authors = Author.all_authors()
    return render_template('book_show.html', book=book, all_authors=all_authors)