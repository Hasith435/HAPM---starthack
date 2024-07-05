from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_STUDENTS = "database_students.db"
# DB_TEACHERS = "database_teachers.db"
# DB_NOTES = "database_notes.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hfdjshgjkfd'

    db_path_students = path.join(app.instance_path, '../website', DB_STUDENTS)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path_students}"

    # db_path_teachers = path.join(app.instance_path, '../website', DB_TEACHERS)
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path_teachers}"

    # db_path_notes = path.join(app.instance_path, '../website', DB_NOTES)
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path_notes}"

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_STUDENTS):
        with app.app_context():
            db.create_all()
            print("Database created")
    else:
        print("STUDENT Database already exists")


    # if not path.exists('website/' + DB_TEACHERS):
    #     with app.app_context():
    #         db.create_all()
    #         print("Database created")
    # else:
    #     print("TEACHER Database already exists")


    # if not path.exists('website/' + DB_NOTES):
    #     with app.app_context():
    #         db.create_all()
    #         print("Database created")
    # else:
    #     print("NOTES Database already exists")