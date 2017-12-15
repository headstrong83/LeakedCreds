# mongo.py

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = 'leeky'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/'

mongo = PyMongo(app)

class user(Resource):
    def get(self, name):
        star = mongo.db.creds
        s = star.find_one({'username' : name})
        if s:
            output = {'username' : s['username'], 'password' : s['password']}
        else:
            output = "No such email"
        return jsonify({'result' : output})

api.add_resource(user, '/user/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
