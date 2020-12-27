from flask import Flask
from flask_restful import Api
from flask_jwt import JWT 
from security import authenticate, identify
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'didier'
api = Api(app)

jwt = JWT(app, authenticate, identify)  # create endpoint: /auth

# im this section we conect APIs to a database.

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)
