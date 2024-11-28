from utils.db import db


class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(100), nullable=False)
    blog_content = db.Column(db.String(1000), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
