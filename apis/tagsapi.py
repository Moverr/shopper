from flask import Blueprint,Flask
 
tagsap = Blueprint('tagsap', __name__)

@tagsap.route('/')
def index():
    return('tags')