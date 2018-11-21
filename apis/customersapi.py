from flask import Blueprint,Flask
 
customersapi = Blueprint('customersapi', __name__)

@customersapi.route('/')
def index():
    return('customers')