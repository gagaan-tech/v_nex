from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# Creating an SQLAlchemy instance
db = SQLAlchemy()
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = db.relationship('Post')
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #github_link = db.Column(db.String(600),unique=True)
    name = db.Column(db.String(100))
    #filename = db.Column(db.String(100))
    category = db.Column(db.String(100))
    username = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    images = db.relationship('Images')

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    github_link = db.Column(db.String(600),unique=True)
    filename = db.Column(db.String(100))
    post = db.Column(db.Integer, db.ForeignKey('post.id'))