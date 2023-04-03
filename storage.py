import os
import json
import tempfile
import argparse

storage_file = os.path.join(tempfile.gettempdir(), "storage.data")

def load_storage():
	if not os.path.exists(storage_file):
		return{}
	with open(storage_file, "r") as f:
		return json.load(f)

def save_storage(storage):
	with open(storage_file, "w") as f:
		json.dump(storage, f)

def add(key, value):
	storage = load_storage()
	print(storage_file)
	if key in storage.keys():
		storage[key].append(value)
	else:
		storage[key] = [value]
	save_storage(storage)

def get(key):
	storage = load_storage()
	return storage.get(key, [])

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--key", help = "key name")
	parser.add_argument("--value", help = "value to add")
	args = parser.parse_args()

	if args.key and args.value:
		add(args.key, args.value)
	elif args.key:
		values = get(args.key)
		print(",".join(values))

