from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import flask_whooshalchemy as wa
# Creates the application object 
app = Flask(__name__)

#download sqlite browser for view all data of website
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
#app.config['WHOOSH_BASE']='whoosh'

db = SQLAlchemy(app)

# Import Views from the app module. 
from app import views
