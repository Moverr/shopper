from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Categories(Model):
    pass

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

    