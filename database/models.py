from database.db import db

#Data Model for Books
class Books(db.Document):
    id = db.IntField(required=True, unique=True)
    author = db.StringField(required=True)    
    country = db.StringField(required=True)
    imageLink = db.StringField(required=True)
    language = db.StringField(required=True)
    link = db.StringField(required=True)
    pages = db.IntField(required=True, unique=True)
    title = db.StringField(required=True)
    year = db.IntField(required=True, unique=True)
