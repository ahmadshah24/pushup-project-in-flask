from flask_login import UserMixin
from __init__ import db
from datetime import datetime

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)
    workouts = db.relationship('Workout',backref='author',lazy=True)
    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return self.is_active

    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     return str(self.id)
    
    def __repr__(self):
        return f'<User id={self.id} email={self.email}>'
    

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer,nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    comment = db.Column(db.Text,nullable=False)  
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)



 