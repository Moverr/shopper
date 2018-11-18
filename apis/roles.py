from flask import Blueprint,Flask
 
tags = Blueprint('roles', __name__)

@tags.route('/')
def index():
    return('roles')