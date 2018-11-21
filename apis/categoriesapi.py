from flask import Blueprint,Flask
 
categoriesapi = Blueprint('categoriesapi', __name__)

@categoriesapi.route('/')
def index():
    return('categories')