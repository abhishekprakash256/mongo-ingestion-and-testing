#imports
import json
import os 
from datetime import timedelta, datetime
from flask import Flask, render_template, request, jsonify, redirect, make_response , url_for, send_from_directory
#from flask_cors import CORS  not needed as per local testing




app = Flask(__name__)


@app.route("/mongo/section/<category>/article/<name>" , methods=["GET"])
def getArticleData(category,name):
	"""
	The function to get the article data from particular category
	"""

	print(category, name)
	return "<h1>Get Mogo Article</h1>"



@app.route("/mongo/section/<category>" , methods=["GET"])
def getSectionData(category):
	"""
	The function to get the section data in cards form
	"""
	
	print(category)

	return "<h1>Get Mongo section data</h1>"


@app.route("/mongo/section/explore" , methods=["GET"])
def getExploreData():
	"""
	The function to get the explore data of mixed sections
	"""
	
	print("explore")

	return "<h1>Get Mongo Explore data</h1>"



@app.route("/mongo/search/<data>" , methods=["GET"])
def getSearchData(data):
	"""
	The function to get the search data
	"""
	
	print(data)

	return "<h1>Get Mongo search data</h1>"









if __name__ == '__main__':
		app.run(port=5000, debug=True)