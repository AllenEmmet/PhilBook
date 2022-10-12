from flask import Flask
from flask_app.controllers import users, posts, books, comments

from flask_app import app


if __name__=='__main__':
    app.run(debug=True, port=5001)
