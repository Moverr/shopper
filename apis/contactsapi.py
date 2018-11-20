from flask import Blueprint,Flask
 
contactsapi = Blueprint('contactsapi', __name__)

@contactsapi.route('/')
def index():
    return('contacts')