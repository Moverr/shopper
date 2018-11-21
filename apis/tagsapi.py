from flask import Blueprint,Flask
 
tagsapi = Blueprint('tagsap', __name__)

@tagsapi.route('/')
def index():
    return('tags')