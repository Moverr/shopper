from flask import Blueprint,Flask
 
tags = Blueprint('users', __name__)

@tags.route('/')
def index():
    return('users')