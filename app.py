from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, abort, Api, Resource
from apis.itemsapi import itemsapi
from apis.categoriesapi import categoriesapi
from apis.tagsapi import tagsapi
from apis.forms.forms import RegistrationForm,LoginForm



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = '3e740fff46cc603965d8e842ded3d21a'

db = SQLAlchemy(app)

app.register_blueprint(itemsapi,url_prefix='/items')
app.register_blueprint(categoriesapi,url_prefix='/categories')
app.register_blueprint(tagsapi,url_prefix='/tags')

api = Api(app)

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

@app.route('/')
def index():
    return render_template('home.html',posts=posts,title='LORD ABOVE')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
   
    if form.validate_on_submit():     
        response = 'Account Created Succesfully'    
        return redirect(url_for('index',success=response))
    else:        
        response = ' Something Went Wrong '

    return render_template('register.html', title='Registration Form',form=form,error=response)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login Form',form=form)



if __name__ == '__main__':
    app.run(debug=True)
