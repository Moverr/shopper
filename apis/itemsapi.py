from flask import Blueprint,Flask
 
itemsapi = Blueprint('itemsapi', __name__)

@itemsapi.route('/')
def index():
    return('ITEMS')