# from . import db
from flask_login import UserMixin
# from sqlalchemy.sql import func

class TutorSubject():
    id = None#db.Column(db.Integer, primary_key=True)
    data = None#db.Column(db.String(20))
    user_id = None##db.Column(db.Integer, db.ForeignKey('user.id'))

class User(UserMixin):
    def __init__(self,row=None) -> None:
        self.user_id=None
        self.username=None
        self.date=None
        self.email=None
        self.hash=None
        self.is_active=True
        if row:
            self.user_id=row[0]
            self.username = row[1]
            self.date = row[2]
            self.email= row[1]
            self.hash = row[6]

        
        
    def get_id(self):
        return str(self.user_id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False
# def create_database():
#     db.create_all()
#     print('Created Database!')
