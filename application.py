from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, abort, Api, Resource
from wsgiref.simple_server import make_server

from apis.itemsapi import itemsapi
from apis.categoriesapi import categoriesapi
from apis.tagsapi import tagsapi
from apis.forms.forms import RegistrationForm,LoginForm



application = Flask(__name__)
# application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
application.config['SECRET_KEY'] = '3e740fff46cc603965d8e842ded3d21a'

# db = SQLAlchemy(application)

application.register_blueprint(itemsapi,url_prefix='/items')
application.register_blueprint(categoriesapi,url_prefix='/categories')
application.register_blueprint(tagsapi,url_prefix='/tags')

api = Api(application)

posts = [
    {
        'author':'Corey Shafer',
        'title':'Blog Post 1',
        'content': '  My First Blog post',
        'date_posted':'Nov 20 2018'

    },
    {
        'author':'Muyinda Rogers',
        'title':'Blog Post 2',
        'content': '  My Second Blog post',
        'date_posted':'Nov 20 2018'

    }
    

]

@application.route('/')
@application.route('/home')
def index():
    return render_template('home.html',posts=posts,title='LORD ABOVE')

@application.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
   

    if form.validate_on_submit():     
        response = 'Account Created Succesfully, Kindly check your email address to confirm '     
        return render_template('register.html', title='Registration Form',form=form,success=response)
    # else:        
    #     response = ' Something Went Wrong '
    #     return render_template('register.html', title='Registration Form',form=form,error=response)

    
    return render_template('register.html', title='Registration Form',form=form)

    

@application.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        if form.email.data =='moverr@gmail.com' and form.password.data == 'password':
            response = 'Account  Logged in successfully '     
            return render_template('login.html', title='Login Form',form=form,success=response)
        else:
            response = 'Invalid Login Credentials  '   
            return render_template('login.html', title='Login Form',form=form,error=response)


    return render_template('login.html', title='Login Form',form=form)



if __name__ == '__main__':
    # application.run()
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()



 
