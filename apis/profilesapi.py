from flask import Blueprint,Flask
 
profilesapi = Blueprint('profilesapi', __name__)

@profilesapi.route('/')
def index():
    return('profiles')