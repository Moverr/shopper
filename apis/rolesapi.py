from flask import Blueprint,Flask
 
rolesapi = Blueprint('rolesapi', __name__)

@rolesapi.route('/')
def index():
    return('roles')