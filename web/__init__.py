from flask import Flask,blueprints
import os
from . import models
from flask_login import LoginManager



# Create app function to create app
def create_app():
    from .view import view
    from .authentication import authentication
    from .user_management import user_management

    app = Flask(__name__)
    UPLOAD_FOLDER = 'file_uploaded'
    DB_NAME = 'database.db'
    
    # adding configuration for using a sqlite database
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY_FOR_FLASK")# for session
    
    models.db.init_app(app)
    app.register_blueprint(view, url_prefix='/')# added blueprint of view.py to show the page
    app.register_blueprint(authentication,url_prefix="/auth")
    app.register_blueprint(user_management,url_prefix='/me')
    login_manager = LoginManager()
    login_manager.login_view = 'authentication.login'
    login_manager.init_app(app)

    from .models import User,Post,Images
    models.db.create_all(app=app)
    #create_database(app,DB_NAME)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    return app


def create_database(app,DB_NAME):
    if not os.path.exists('web/' + DB_NAME):
        models.db.create_all(app=app)
        print('Created Database!')
