from crypt import methods
from operator import methodcaller
from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.post import Post
from flask_app.models import user
from flask_app.models.comment import Comment
  
@app.route('/publish', methods=["POST"])
def publish():
    content = request.form["content"]
        
        
        
    if len(content) < 10:
        flash('Post must be at least 10 characters', 'new')
        return redirect('/dashboard')
        
    data = {
        "content": content,
            
            
        "user_id": session['user'],

        "book_id": session['book']
    }
    Post.save(data)
    return redirect('/dashboard')

@app.route('/post/<int:id>')
def showPost(id):
    data = {
        'id': id
    }
    user_data = {
        'id': session['user']
    }
    session['post'] = id
    post=Post.get_post(data)
   
    return render_template('post.html', post = post, user=user.User.get_one_id(user_data), comments=Comment.get_comments(data))

@app.route('/post/delete/<int:id>', methods=["POST"])
def delete(id):
    data = {
        "id": id
    }
    Post.delete_post(data)
    return redirect ('/dashboard')

@app.route('/post/update/<int:id>', methods=["POST"])
def update(id):
    data ={
        "id":id 
    }
    
    return render_template('update_post.html', post= Post.get_post(data))

@app.route('/post/edit/<int:id>', methods=["POST"])
def edit(id):
    data ={
        "id":id,
        'content': request.form['content'],
        
    }
    Post.update_post(data)
    
    return redirect('/dashboard')