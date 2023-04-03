import os
import json
import tempfile
import argparse

from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

storage_file = os.path.join(tempfile.gettempdir(), "storage.data")

app = Flask(__name__)
api = Api(app)

def load_storage():
	if not os.path.exists(storage_file):
		return{}
	with open(storage_file, "r") as f:
		return json.load(f)

def save_storage(storage):
	with open(storage_file, "w") as f:
		json.dump(storage, f)

def get(key):
	storage = load_storage()
	return storage.get(key, [])

class Quote(Resource):
	def get(self, id=None):
		storage = load_storage()
		if id == None:
			return storage, 200
		for key in storage.keys():
			if(key == id):
				return storage[key], 200
		return "Result not found", 404

api.add_resource(Quote, "/api", "/api/", "/api/read<string:id>")

@app.route('/')
def index():
	return "<h1>key_value</h1> <p>GET /key-values/&lt;key&gt;; - 111</p>"

if __name__ == '__main__':
	app.run(debug=True)	
