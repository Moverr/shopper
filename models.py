import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date,Enum,DateTime
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from enums.statusenum   import StatusEnum
from app import db

class Categories(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), nullable=False)
    status =  db.Column(Enum(StatusEnum))
    author_id = db.Column(Integer, nullable=False)    
    date_created = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_by = db.Column(Integer)
    date_updated = db.Column(DateTime)

class Contacts(Model):
    pass

class FeaturedItems(Model):
    pass

class FeatureTypes(Model):
    pass

class Items(Model):
    pass

class ItemTags(Model):
    pass

class Permissions(Model):
    pass;

class Roles(Model):
    pass

class Tags(Model):
    pass

class UserRoles(Model):
    pass

class Users(Model):
    pass

