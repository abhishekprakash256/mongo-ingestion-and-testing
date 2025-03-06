"""
The data insertion file for testing purpose
"""

import mongo_helper_kit
from test_data import article_test_data


#constansts
DB_NAME = "test-main-database"
COLLECTION_NAME = "test-article-collections"
MONGO_HOST_NAME = "localhost"

#helper method instance
db_helper = mongo_helper_kit.Helper_fun(MONGO_HOST_NAME)

#make the database 
#db_helper.make_database_and_collection(DB_NAME, COLLECTION_NAME)

#insert the data
#db_helper.insert_data(DB_NAME, COLLECTION_NAME,article_test_data )


#get the data , change to return the data  
#db_helper.show_all_data(DB_NAME, COLLECTION_NAME)


#get the article data 
res = db_helper.show_article_data(DB_NAME, COLLECTION_NAME, {'article_name':"test1"})

print(res)