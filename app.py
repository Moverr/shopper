from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, abort, Api, Resource
from apis.itemsapi import itemsapi
from apis.categoriesapi import categoriesapi
from apis.tagsapi import tagsapi



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db";
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



if __name__ == '__main__':
    app.run(debug=True)
