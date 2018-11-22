from flask import Flask
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

@app.route('/')
def index():
    return ("Did YOu Know ")



if __name__ == '__main__':
    app.run(debug=True)
