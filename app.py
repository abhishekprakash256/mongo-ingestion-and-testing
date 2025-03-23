#imports
import json
import os 
from datetime import timedelta, datetime
from flask import Flask, Response , render_template, request, jsonify, redirect, make_response , url_for, send_from_directory
import mongo_helper_kit
from bson import json_util



#constansts the database and the collection name will change in the actual implemntations 
#mongo database infomation
DB_NAME = "test-main-database"
COLLECTION_NAME = "test-article-collections"
MONGO_HOST_NAME = "localhost"
SECTION_NAME = ["tech", "project", "life"]



#helper method instance
db_helper = mongo_helper_kit.Helper_fun(MONGO_HOST_NAME)



#make the database 
app = Flask(__name__)




@app.route("/mongo/section/<category>/article/<article_name>" , methods=["GET"])  
def getArticleData(category,article_name):
	"""
	The function to get the article data from particular category
	"""

	data = db_helper.get_article_data(DB_NAME, COLLECTION_NAME, category, article_name)

	article_data = json.loads(json_util.dumps(data))  #the json utils makes the object id parse in json format from mongo

	return jsonify(article_data)
	



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

	data = db_helper.get_card_data(DB_NAME, COLLECTION_NAME, category, limit)

	return jsonify(data)



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
	
	data_section_one = db_helper.get_card_data(DB_NAME, COLLECTION_NAME,SECTION_NAME[0], limit = 5)
	data_section_two = db_helper.get_card_data(DB_NAME, COLLECTION_NAME, SECTION_NAME[1], limit = 5)
	data_section_three = db_helper.get_card_data(DB_NAME, COLLECTION_NAME,SECTION_NAME[2], limit = 5)
	
	return jsonify(data_section_one + data_section_two + data_section_three)



@app.route("/mongo/search/<keyword>" , methods=["GET"])
def getSearchData(keyword):
	"""
	The function to get the search data
	"""
	
	data = db_helper.search_database(DB_NAME, COLLECTION_NAME, keyword)

	return jsonify(data)









if __name__ == '__main__':
		app.run(port=5000, debug=True)