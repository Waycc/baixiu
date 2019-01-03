import app
from settings import settings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = "person"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("_class.id"), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Class(db.Model):
    __tablename__ = '_class'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), nullable=False)
    persons = db.relationship('Person', backref='_class', lazy=True)

db.create_all()
