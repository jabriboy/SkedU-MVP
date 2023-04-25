from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    rotation = db.relationship('Rotation')


class Rotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    
    tue_switch = db.Column(db.String(50))
    tue_joystick = db.Column(db.String(50))
    tue_notebook = db.Column(db.String(50))
    tue_camera = db.Column(db.String(50))

    wed_switch = db.Column(db.String(50))
    wed_joystick = db.Column(db.String(50))
    wed_notebook = db.Column(db.String(50))
    wed_camera = db.Column(db.String(50))

    thu_switch = db.Column(db.String(50))
    thu_joystick = db.Column(db.String(50))
    thu_notebook = db.Column(db.String(50))
    thu_camera = db.Column(db.String(50))

    fri_switch = db.Column(db.String(50))
    fri_joystick = db.Column(db.String(50))
    fri_notebook = db.Column(db.String(50))
    fri_camera = db.Column(db.String(50))

    sun_m_switch = db.Column(db.String(50))
    sun_m_joystick = db.Column(db.String(50))
    sun_m_notebook = db.Column(db.String(50))
    sun_m_camera = db.Column(db.String(50))

    sun_e_switch = db.Column(db.String(50))
    sun_e_joystick = db.Column(db.String(50))
    sun_e_notebook = db.Column(db.String(50))
    sun_e_camera = db.Column(db.String(50))

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    rotation_id = db.Column(db.Integer, db.ForeignKey('rotation.id'), unique=True)
    days_id = db.Column(db.Integer, db.ForeignKey('days.id'))
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'))

    name = db.Column(db.String(50))

class Days(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    day = db.Column(db.String(50))

class Positions(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    position = db.Column(db.String(50))

