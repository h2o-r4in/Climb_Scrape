# (1)get all json files in directory (2) for each json file, grab contents of text (3) run matcher on the files (4) return true 

import json
from os import listdir
from os.path import isfile, join
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


def getjsonfiles(): 
	allfiles = [f for f in listdir('.') if isfile(join('.', f))]
	jsonfiles = []
	for x in allfiles: 
		if '.json' in x: 
			jsonfiles.append(x)
	return jsonfiles

def minnewaska_is_open(text):
	if "Minnewaska is closed to boating, scuba diving, equestrian use, climbing and bouldering until further notice." not in text:
		return True
	else:
		return False

@app.route('/minnewaska')
def get_statuses():
	# returns dictionary of placename: status
	statuses = ""
	for jsonfile in getjsonfiles():
		placename, fileformat = jsonfile.split(".")

		with open(jsonfile) as json_file:
			data = json.load(json_file)

			# data = [{}, {}, ]
			if jsonfile == "minnewaska.json":
				for element in data:
					print("minnewaska open?")
					if minnewaska_is_open(element["text"]):
						statuses = "Yes"
					else:
						statuses = "No!"


	return statuses


# def hello_world():
#     return 'Hello, World!'


# print(get_statuses())


