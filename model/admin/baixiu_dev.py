from app import app
from settings import settings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(20), unique=True, nullable=False, )
    email = db.Column(db.String(120), unique=True, nullable=False)
    nickname = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(20), nullable=True)
    avatar = db.Column(db.String(120), nullable=True, default="/static/uploads/avatar.jpg")
    bio = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(20), nullable=False, default="activated")
    # class_id = db.Column(db.Integer, db.ForeignKey("_class.id"), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def to_dict(self):
        return {
            "id": self.id,
            "slug": self.slug,
            "email": self.email,
            "nickname": self.nickname,
            "avatar": self.avatar,
            "bio": self.bio,
            "status": self.status
        }


# class Class(db.Model):
#     __tablename__ = '_class'
#     __table_args__ = {'mysql_collate': 'utf8_general_ci'}
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(24), nullable=False)
#     persons = db.relationship('Person', backref='_class', lazy=True)
#
# db.create_all()
