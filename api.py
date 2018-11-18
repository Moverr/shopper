from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from apis.items import items

app = Flask(__name__)
app.register_blueprint(items,url_prefix='/items')
api = Api(app)

@app.route('/')
def method_name():
    return ("Did YOu Know ")



if __name__ == '__main__':
    app.run(debug=True)
