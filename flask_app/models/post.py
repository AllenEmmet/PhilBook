from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import user
from flask_app.models import comment
from flask_app.models import book

from flask import render_template, redirect, request, session, flash

class Post:
    db = "newPhil"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.book_id = data['book_id']
        self.user = None
        self.book=None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (content, user_id, book_id) VALUES (%(content)s, %(user_id)s, %(book_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM posts JOIN users on posts.user_id=users.id JOIN books on posts.book_id = books.id;"
        results = connectToMySQL(cls.db).query_db(query)
        
        posts = []
        for row in results:
            post = cls(row)
            user_data = {
                'id': row['users.id'], 
                'first_name': row['first_name'], 
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            books_data = {
                'id': row['books.id'],
                'title': row['title'],
                'author': row['author']
            }
            postUser = user.User(user_data)
            post.user = postUser
            postBook = book.Book(books_data)
            post.book = postBook
            posts.append(post)
            
        return posts
  
    @classmethod
    def get_post(cls, data):
        query="SELECT * FROM posts JOIN users on posts.user_id=users.id JOIN books on posts.book_id = books.id WHERE posts.id=%(id)s;"
        results= connectToMySQL(cls.db).query_db(query, data)[0]
        post = cls(results)
        user_data = {
                'id': results['users.id'], 
                'first_name':results['first_name'], 
                'last_name':results['last_name'],
                'email':results['email'],
                'password':results['password'],
                'created_at': results['users.created_at'],
                'updated_at':results['users.updated_at']
            }
        books_data = {
                'id': results['books.id'],
                'title': results['title'],
                'author': results['author']
            }
        postUser = user.User(user_data)
        post.user = postUser
        postBook = book.Book(books_data)
        post.book = postBook
        return post
        
        

    @classmethod
    def delete_post(cls, data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
      
        print(data)
       
        return connectToMySQL(cls.db).query_db(query, data)
        
    @classmethod
    def update_post(cls, data):
        query = 'UPDATE posts SET content = %(content)s WHERE id = %(id)s;'
        print('update working')
        return connectToMySQL(cls.db).query_db(query, data)