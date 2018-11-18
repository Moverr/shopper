from flask import Blueprint,Flask
 
customers = Blueprint('customers', __name__)

@customers.route('/')
def index():
    return('customers')