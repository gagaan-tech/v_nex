from web import create_app, models
from web.models import db

app = create_app()# calling from init.py

if __name__ == '__main__':
    
    app.run()