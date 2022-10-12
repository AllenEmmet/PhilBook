from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.post import Post
from flask_app.models import user
from flask_app.models import comment

@app.route('/comment/pub', methods=["POST"])
def pub_comment():
    postID = session['post']
    content=request.form["content"]
    data = {
        "content" : content,
        "user_id" : session['user'],
        "post_id" : postID
    }
    
    comment.Comment.save(data)
    return redirect (f'/post/{postID}')

@app.route('/comment/delete', methods=["POST"])
def deletep():
    postID = session['post']
    comment.Comment.delete_comment(request.form)
    return redirect (f'/post/{postID}')