import os
import json
import tempfile
import argparse

from flask import Flask, request, jsonify
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

class Read(Resource):
	def get(self):
		storage = load_storage()
		key = request.args.get('key')
		print(key)
		if key == None:
			return storage, 200
		for key in storage.keys():
			return storage[key], 200
		return "Result not found", 404

class Write(Resource):
	def post(self):
		storage = load_storage()
		key = request.args.get('key')
		value = request.args.get('value')
		print(request)
		if not key:
			return jsonify({'error': 'no key'})
		if not value:
			return jsonify({'error': 'no value'})
		if key in storage.keys():
			storage[key].append(value)
			save_storage(storage)
			return jsonify({'value append -': ' '.join(storage[key]) })
		else:
			storage[key] = [value]
		save_storage(storage)

api.add_resource(Read, "/api", "/api/", "/api/read")
api.add_resource(Write, "/api/write")

@app.route('/')
def index():
	return "<h1>key_value</h1> <p>GET /key-values/&lt;key&gt;; - 111</p>"

if __name__ == '__main__':
	app.run(debug=True)	
