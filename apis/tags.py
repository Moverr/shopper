from flask import Blueprint,Flask
 
tags = Blueprint('tags', __name__)

@tags.route('/')
def index():
    return('tags')