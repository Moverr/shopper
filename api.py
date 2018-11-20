from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from apis.itemsapi import itemsapi
from apis.categoriesapi import categoriesapi
from apis.tagsapi import tagsapi



app = Flask(__name__)
app.register_blueprint(items,url_prefix='/items')
app.register_blueprint(categories,url_prefix='/categories')
app.register_blueprint(tags,url_prefix='/tags')

api = Api(app)

@app.route('/')
def method_name():
    return ("Did YOu Know ")



if __name__ == '__main__':
    app.run(debug=True)
