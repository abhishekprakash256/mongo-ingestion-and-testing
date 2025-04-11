#imports
import json
import datetime
from flask import current_app, Flask, Response , render_template, request, jsonify, redirect, make_response , url_for, send_from_directory
import mongo_helper_kit
from bson import json_util
import pgsql_helper_kit
import redis_helper_kit
import hash_utils
import jwt
import hmac

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


#redis database information
REDIS_HOST_NAME = "localhost"
REDIS_HASH_NAME = "test_hash"
REDIS_SET_NAME = "test_set"




#make the helper instance
pgsql_engine , pgsql_session = pgsql_helper_kit.create_db_session(host_name = PGSQL_HOST_NAME, db_name = PGSQL_DB_NAME, user_name = PGSQL_USER_NAME, password = PGSQL_PASSWORD)


db_helper_pgsql = pgsql_helper_kit.Db_Helper(pgsql_session, pgsql_engine)


#helper method instance
db_helper_mongo = mongo_helper_kit.Helper_fun(MONGO_HOST_NAME)

#make the redis instance 
db_helper_redis = redis_helper_kit.Helper_fun(hash_name= REDIS_HOST_NAME, set_name= REDIS_SET_NAME , host_name= REDIS_HOST_NAME)






#make the database 
app = Flask(__name__)

# Secret key for JWT encoding & decoding
app.config['SECRET_KEY'] = 'your_secret_key' #change this later







@app.route("/" , methods=["GET"])
def home():
    """
    The home page of the CMS
    """
    return "<h1>Welcome to the CMS</h1>"


#------------------------------mongo methods --------------------------------

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


#------------------------------mongo methods -------------------------------- ends


#----------------------------------pgsql methods ------------------------------------



# Function to generate JWT token
def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Corrected utcnow()
    }
    secret_key = current_app.config['SECRET_KEY']  # Using current_app for Flask apps
    return jwt.encode(payload, secret_key, algorithm="HS256")


def compare_tokens(token1, token2):
    if hmac.compare_digest(token1, token2):
        return True
    return False



@app.route("/pgsql/login", methods=["POST"])
def get_login_data():
    """
    Secure login function using a POST request to authenticate the user
    """
    data = request.get_json()
    
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"status": "error", "message": "Missing username or password."}), 400

    #check if user exists in the database 
    if db_helper_pgsql.check_user_exists(username):

        #confirm the login 
        hashed_stored_password = db_helper_pgsql.get_user_password(username)

        if db_helper_pgsql.verify_password(password, hashed_stored_password) :

            access_token = generate_token(username)
            
            return jsonify({
                            "status": "success",
                            "message": "Login successful.",
                            "access_token": access_token,
                            "user": {
                                "username": username,
                            }
                        }), 200
        else:

            return jsonify({"status": "error", "message": "Invalid username or password."}), 401


    else :

        return jsonify({"status": "error", "message": "Invalid username or password."}), 401


@app.route("/pgsql/signup", methods=["POST"])
def sign_up():
    """
    The sign up for the user using unique username and password
    """

    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
    
    username = data.get("username")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    #check if the username exists
    if db_helper_pgsql.check_user_exists(username):

        return jsonify({"status": "error", "message": "Username Already exists use a different user name"}), 400
    
    else:

        if password == confirm_password :

            #added the redis  hash suport
            hash_utils.generate_unique_hash(REDIS_HOST_NAME,REDIS_SET_NAME ,REDIS_HOST_NAME ,5,10,100)

            userhash = db_helper_redis.pop_set_val()
            
            #print(userhash)

            db_helper_pgsql.create_user(username, password , userhash)

            return jsonify({"status": "success", "user_token" : userhash, "message": "User registered"}) , 201
        
        else:

            return jsonify({"status": "error", "message": "Passwords do not match"}), 400



@app.route("/pgsql/update", methods=["PUT"])
def update_password():
    """
    Updates the user's password verify the user details and check the new credentails as well
    """
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400

    username = data.get("username")
    old_password = data.get("old_password")
    new_password = data.get("new_password")
    confirm_password = data.get("confirm_password")

    # Validate required fields
    if not username or not old_password or not new_password:
        return jsonify({"status": "error", "message": "All fields are required"}), 400

    # Verify if the user exists
    if not db_helper_pgsql.check_user_exists(username):
        return jsonify({"status": "error", "message": "User not found"}), 404
    
    #verify the new password
    if new_password != confirm_password :
        return jsonify({"status": "error", "message": "New Password not match"}), 400

    #get the stored password
    hashed_stored_password = db_helper_pgsql.get_user_password(username)

    if not db_helper_pgsql.verify_password(old_password, hashed_stored_password) :
        
        return jsonify({"status": "error", "message": "Incorrect old password"}), 401
    
    #update the password
    db_helper_pgsql.update_user_password(username , new_password)

    return jsonify({"status": "success", "message": "Password updated successfully"}), 200

 
@app.route("/pgsql/recover", methods=["PUT"])
def recover_password():
    """
    Updates the user's password verify the user details and check the new credentails as well
    """
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400

    username = data.get("username")
    token = data.get("token")
    new_password = data.get("new_password")
    confirm_password = data.get("confirm_password")

    # Verify if the user exists
    if not db_helper_pgsql.check_user_exists(username):
        return jsonify({"status": "error", "message": "User not found"}), 404
    
    #verify the new password
    if new_password != confirm_password :
        return jsonify({"status": "error", "message": "New Password not match"}), 400

    #verify if the token matches 
    stored_token = db_helper_pgsql.get_user_hash(username)
    
    if not compare_tokens(stored_token , token) :

        return jsonify({"status": "error", "message": "Invalid Token"}), 400

    #update the password
    db_helper_pgsql.update_user_password(username , new_password)

    return jsonify({"status": "success", "message": "Password updated successfully"}), 200


@app.route("/pgsql/delete-d", methods=["DELETE"])
def delete_user_d():
    """
    Deletes the user's account after verifying the token and password.
    """
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400

    username = data.get("username")
    password = data.get("password")
    token = data.get("token")

    # Verify if the user exists
    if not db_helper_pgsql.check_user_exists(username):
        return jsonify({"status": "error", "message": "User not found"}), 404

    #verify if the token matches 
    stored_token = db_helper_pgsql.get_user_hash(username)
    
    if not compare_tokens(stored_token , token) :
        return jsonify({"status": "error", "message": "Invalid Token"}), 400
    
    #get the stored password
    hashed_stored_password = db_helper_pgsql.get_user_password(username)

    if not db_helper_pgsql.verify_password(password, hashed_stored_password) :
        
        return jsonify({"status": "error", "message": "Incorrect password"}), 401

    #delete the user
    db_helper_pgsql.delete_user(username)

    return jsonify({"status": "success", "message": "User account deleted successfully"}), 200

    

#---------------------------------the new method for the database access-------------------------

@app.route("/pgsql/create_user", methods=["POST"])
def create_user():
    """
    The function to create the user in data base
    """
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
    
    username = data.get("username")
    password = data.get("password")

    hash_utils.generate_unique_hash(REDIS_HOST_NAME,REDIS_SET_NAME ,REDIS_HOST_NAME ,5,10,100)

    user_token = db_helper_redis.pop_set_val()

    if db_helper_pgsql.create_user(username, password , user_token): 

        return jsonify({"status": "success", "user_token" : user_token, "message": "User registered"}) , 201

    return jsonify({"status": "error", "message": "User not regisred"}), 400


@app.route("/pgsql/check_user", methods=["POST"])
def check_user_exists():
    """
    Check if the user exists in the database 
    """
    data = request.get_json()
    
    if not data or "username" not in data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
    
    username = data.get("username")
    exists = db_helper_pgsql.check_user_exists(username=username)

    return jsonify({
        "status": "success",
        "userExists": exists,
        "message": "User exists" if exists else "User does not exist",
        "username": username,
    }), 200




@app.route("/pgsql/verify_password", methods=["POST"])
def verify_password():
    """
    To check if the user has given correct password
    takes the hashed password 
    takse the user password passed
    """
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400

    hashed_password = data.get("hashed_password")
    passed_password = data.get("passed_password")

    if db_helper_pgsql.verify_password(passed_password, hashed_password) :

        return jsonify({"status": "success", "message": "Password Match"}), 200
    
    return jsonify({"status": "error", "message": "Invalid password"}), 400



@app.route("/pgsql/get_user_password", methods=["POST"])
def get_user_password():
    """
    The function to get the user password
    """

    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
    
    #chek the user
    username = data.get("username") 
    
    hashed_stored_password = db_helper_pgsql.get_user_password(username)

    if hashed_stored_password :

        return jsonify({"status": "success", "hashed_password": hashed_stored_password}), 200
    
    return jsonify({"status": "error", "message": "Password not found"}), 404 



@app.route("/pgsql/update_user_password", methods=["POST"])
def update_user_password():
    """
    The function to update the user password
    """

    print("update user password")

    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
    
    username = data.get("username")
    newPassword = data.get("newPassword")

    print(username , "the new password",newPassword)

    if db_helper_pgsql.update_user_password(username , newPassword) :

        return jsonify({"status": "success", "message": "Password updated successfully"}), 200
    
    return jsonify({"status": "error", "message": "Password update failed"}), 400



@app.route("/pgsql/get_user_token", methods=["POST"])
def get_user_token():
    """
    The function to get the user token
    """
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
    
    username = data.get("username")

    user_token = db_helper_pgsql.get_user_hash(username)

    if user_token :

        return jsonify({"status": "success", "user_token": user_token}), 200
    
    return jsonify({"status": "error", "message": "no token found"}), 404



@app.route("/pgsql/delete_user", methods=["DELETE"])
def delete_user():
    """
    The function to delete the user
    """
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400

    username = data.get("username") 

    if db_helper_pgsql.delete_user(username) :

        return jsonify({"status": "success", "message": "User account deleted successfully"}), 200 

    return  jsonify({"status": "error", "message": "User not deleted"}), 400






if __name__ == '__main__':
        app.run(port=5000, debug=True)