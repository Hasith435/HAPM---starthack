from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Users/hasithdewmina/Documents/Hackathons/Start Hack/brew-crew-7690e-firebase-adminsdk-jpqbd-5cfd159577.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hfdjshgjkfd'


    #initializing firestore database
    

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
