from settings import settings
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    alias = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(20), nullable=True)
    img_url = db.Column(db.String(120), nullable=True, default="/static/uploads/avatar.jpg")
    status = db.Column(db.String(20), nullable=False, default="activated")
    # class_id = db.Column(db.Integer, db.ForeignKey("_class.id"), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "alias": self.alias,
            "img_url": self.img_url,
            "status": self.status
        }


class Comment(db.Model):
    __tablename__ = "comments"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False, default=0)  # 0代表作者不是平台注册用户
    created = db.Column(db.DateTime, default=datetime.now())
    content = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=True, default="activated")
    post_id = db.Column(db.Integer, nullable=True)  # 文章id
    parent_id = db.Column(db.Integer, nullable=True, default=0)  # 评论id, 顶级评论为0

    def to_dict(self):
        return {
            "id": self.id,
            "alias": self.alias,
            "created": self.created,
            "content": self.content,
            "status": self.status,
            "post_id": self.post_id,
            "parent_id": self.parent_id,
            "author_id": self.author_id
        }


class Post(db.Model):
    __tablename__ = "posts"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    tags = db.Column(db.String(300))
    created = db.Column(db.DateTime, default=datetime.now())
    views = db.Column(db.String(300))
    content = db.Column(db.Text)
    updated = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, nullable=False, default=0)  # 0代表作者不是平台注册用户
    category_id = db.Column(db.Integer)
    status = db.Column(db.String(20), nullable=True, default="activated")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "tags": self.tags,
            "created": self.created,
            "views": self.views,
            "content": self.content,
            "updated": self.updated,
            "author_id": self.author_id,
            "status": self.status
        }


class Category(db.Model):
    __tablename__ = "categories"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True)
    des = db.Column(db.String(200))
    name = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "des": self.des,
            "name": self.name
        }

# class Class(db.Model):
#     __tablename__ = '_class'
#     __table_args__ = {'mysql_collate': 'utf8_general_ci'}
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(24), nullable=False)
#     persons = db.relationship('Person', backref='_class', lazy=True)
#
#db.create_all()
