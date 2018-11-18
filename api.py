from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

 
@app.route('/items')
def get_items():
    pass

@app.route('/items')
def add_item():
    pass

@app.route('/items/id/<id/>')
def get_item(id):
    pass
    
@app.route('/items/archive/id/<id/>')
def archive_item():
    pass



if __name__ == '__main__':
    app.run(debug=True)
