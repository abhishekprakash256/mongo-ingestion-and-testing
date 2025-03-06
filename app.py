#imports
import json
import os 
from datetime import timedelta, datetime
from flask import Flask, render_template, request, jsonify, redirect, make_response , url_for, send_from_directory
#from flask_cors import CORS  not needed as per local testing
import mongo_helper_kit

#constansts
DB_NAME = "main-database"
COLLECTION_NAME = "article-collections"
MONGO_HOST_NAME = "localhost"

#helper method instance
helper_fun = mongo_helper_kit.Helper_fun(MONGO_HOST_NAME)


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
	should have a min limit of 3 and max to all 
	http://localhost:5000/mongo/section/tech?limit=2
	"""
	
	#make the limit
	limit = request.args.get("limit", type=int)

	if limit is None or limit < 3:
		limit = 3

	return "The data fetched from mongo for section"


@app.route("/mongo/section/explore" , methods=["GET"])
def getExploreData():
	"""
	The function to get the explore data of mixed sections
	get the max data of 15 cards
	"""
	#make the limit
	limit = request.args.get("limit", type=int)
	
	if limit is None or limit < 3:
		limit = 15
	
	return "Get the explore card data from the Mongo with mixed topic"



@app.route("/mongo/search/<data>" , methods=["GET"])
def getSearchData(data):
	"""
	The function to get the search data
	"""
	
	print(data)

	return "<h1>Get Mongo search data</h1>"









if __name__ == '__main__':
		app.run(port=5000, debug=True)