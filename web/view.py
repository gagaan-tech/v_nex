from flask import Blueprint, render_template, request, flash,redirect,url_for,session,send_file
from werkzeug.utils import secure_filename # for files uploading
import os
from flask_login import login_required, current_user
from .models import Post

view = Blueprint('view',__name__,template_folder='templates') # adding blueprint

@view.route('/about')
def home():
    post = [post.category for post in Post.query.all()]
    post = list(set(post))
    return render_template('home.html',user=current_user,post=post)

@view.route('/',methods=['POST'])
def look_image():
    category=request.form.get("categoryselector")
    post = [i for i in Post.query.filter_by(category=category).all()]
    post_no = len(post)
    #https://raw.githubusercontent.com/gagaan-tech/v_nex_data/main/file_uploaded/Marshanicky.png
    posts_category = [post.category for post in Post.query.all()]
    posts_category = list(set(posts_category))
    return render_template('looks.html',posts_category=posts_category,post=post,post_no=post_no,category=category)
    

@view.route('/')
def look():
    post = [post.category for post in Post.query.all()]
    post = list(set(post))
    return render_template('looks.html',posts_category=post,category="Select Category ->")
