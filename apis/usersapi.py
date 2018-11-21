from flask import Blueprint,Flask
 
usersap = Blueprint('usersap', __name__)

@usersap.route('/')
def index():
    return('users')