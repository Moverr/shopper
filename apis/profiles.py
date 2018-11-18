from flask import Blueprint,Flask
 
profiles = Blueprint('profiles', __name__)

@tags.route('/')
def index():
    return('profiles')