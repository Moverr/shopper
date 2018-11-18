from flask import Blueprint,Flask
 
categories = Blueprint('categories', __name__)

@categories.route('/')
def index():
    return('categories')