from . import db
from flask import current_app
from flask_login import UserMixin
from . import db

class TutorSubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique =True)
    password = db.Column(db.String(150))
    certifiedTutor = db.relationship('TutorSubject')

def create_database():
    with current_app.app_context():
        db.create_all()
        print('Created Database!')
