from flask import Blueprint,Flask
 
items = Blueprint('items', __name__)

@items.route('/')
def index():
    return('ITEMS')