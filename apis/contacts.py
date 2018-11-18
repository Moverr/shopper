from flask import Blueprint,Flask
 
tags = Blueprint('contacts', __name__)

@tags.route('/')
def index():
    return('contacts')