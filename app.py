#imports
import json
import os 
from datetime import timedelta, datetime
from flask import Flask, Response , render_template, request, jsonify, redirect, make_response , url_for, send_from_directory
import mongo_helper_kit
from bson import json_util
import pgsql_helper_kit



#constansts the database and the collection name will change in the actual implemntations 
#mongo database infomation
MONGO_DB_NAME = "test-main-database"
MONGO_COLLECTION_NAME = "test-article-collections"
MONGO_HOST_NAME = "localhost"
MONGO_SECTION_NAME = ["tech", "project", "life"]


#pgsl database information
PGSQL_DB_NAME = "test_db"
PGSQL_USER_NAME = "abhi"
PGSQL_HOST_NAME = "localhost"
PGSQL_PASSWORD = "mysecretpassword"




#make the helper instance
pgsql_engine , pgsql_session = pgsql_helper_kit.create_db_session(host_name = PGSQL_HOST_NAME, db_name = PGSQL_DB_NAME, user_name = PGSQL_USER_NAME, password = PGSQL_PASSWORD)


db_helper_pgsql = pgsql_helper_kit.Db_Helper(pgsql_session, pgsql_engine)


#helper method instance
db_helper_mongo = mongo_helper_kit.Helper_fun(MONGO_HOST_NAME)









#make the database 
app = Flask(__name__)

@app.route("/" , methods=["GET"])
def home():
	"""
	The home page of the website
	"""
	return "<h1>Welcome to the home page</h1>"


@app.route("/mongo/section/<category>/article/<article_name>" , methods=["GET"])  
def getArticleData(category,article_name):
	"""
	The function to get the article data from particular category
	"""

	data = db_helper_mongo.get_article_data(MONGO_DB_NAME, MONGO_COLLECTION_NAME, category, article_name)

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

	data = db_helper_mongo.get_card_data(MONGO_DB_NAME, MONGO_COLLECTION_NAME, category, limit)

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
	
	data_section_one = db_helper_mongo.get_card_data(MONGO_DB_NAME, MONGO_COLLECTION_NAME,MONGO_SECTION_NAME[0], limit = 5)
	data_section_two = db_helper_mongo.get_card_data(MONGO_DB_NAME, MONGO_COLLECTION_NAME, MONGO_SECTION_NAME[1], limit = 5)
	data_section_three = db_helper_mongo.get_card_data(MONGO_DB_NAME, MONGO_COLLECTION_NAME,MONGO_SECTION_NAME[2], limit = 5)
	
	return jsonify(data_section_one + data_section_two + data_section_three)



@app.route("/mongo/search/<keyword>" , methods=["GET"])
def getSearchData(keyword):
	"""
	The function to get the search data
	"""
	
	data = db_helper_mongo.search_database(MONGO_DB_NAME, MONGO_COLLECTION_NAME, keyword)

	return jsonify(data)


@app.route("/pgsql/login", methods=["POST"])
def get_login_data():
    """
    Secure login function using a POST request
    """
    data = request.get_json()
    
    if not data or "username" not in data or "password" not in data:
        return jsonify({"message": "Invalid request"}), 400
    
    username = data["username"]
    password = data["password"]

    user_password = db_helper_pgsql.get_user_password(username)

    if user_password is None:
        return jsonify({"message": "User not found"}), 404

    if user_password == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Login failed"}), 401







if __name__ == '__main__':
		app.run(port=5000, debug=True)