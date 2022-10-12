from flask import render_template, redirect, request, session, flash
from flask_app.models import book
from flask_app import app

from flask_app.models.post import Post
from flask_app.models.user import User
from flask_app.models.book import Book

@app.route('/savebook', methods=["POST"])
def saveBook():
    title = request.form['title'], 
    author = request.form['author']
    data = {
        "title": title,
        "author": author
    }
    book.Book.save(data)
    return redirect('/books')

@app.route('/books', methods=["GET","POST"])
def showBooks():
    user_data = {
        'id': session['user']
    }
    return render_template('books.html', books=book.Book.getAll(), user = User.get_one_id(user_data))

@app.route('/setbook', methods=["POST"])
def setBook():
    id = request.form['book_id']
    print(id)
    session['book'] = int(id)
    print(session['book'])
    return redirect('/dashboard/post')

@app.route('/dashboard/post')
def welcome2():
    if 'user' not in session:
        return redirect ('/')
    user_data = {
        'id': session['user']
    }
    if 'book' not in session:
        book_data = {
            
        }
    else:
        book_data = {
            'id': session['book']
        }
    
    return render_template('dashboard2.html', user = User.get_one_id(user_data), posts=Post.getAll(), book=Book.get_one_id(book_data))