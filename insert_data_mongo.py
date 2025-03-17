"""
The data insertion file for testing purpose will be deleted after the features are added
"""

import mongo_helper_kit
from test_data import article_test_data
import inspect

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

#delete all the data 
#db_helper.delete_db(DB_NAME)


#get the data , change to return the data  
db_helper.show_all_data(DB_NAME, COLLECTION_NAME)


#get the article data 
#res = db_helper.show_article_data(DB_NAME, COLLECTION_NAME, {'article_name':"test1"})

#db_helper.show_all_data(DB_NAME, COLLECTION_NAME)


#res = db_helper.get_article_data(DB_NAME, COLLECTION_NAME, "tech", "test2")

#print(res)

#make the index in the data base 




def make_index():
    client = db_helper.mongo_client

    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    db.collection.create_index([
        ("article_name", "text"),
        ("section_name", "text"),
        ("article_para", "text"),
        ("article_data.title", "text"),
        ("article_data.article_para", "text"),
        ("article_data.markdown_data", "text")
    ])




def search_articles(keyword, db_name= DB_NAME, collection_name= COLLECTION_NAME):
    """
    Search articles in MongoDB using a regex-based approach.
    
    :param keyword: The keyword to search for (case-insensitive).
    :param db_name: Name of the database.
    :param collection_name: Name of the collection.
    :return: List of matching documents.
    """

    # Connect to MongoDB (Modify connection string if needed)
    client = db_helper.mongo_client
    db = client[db_name]
    collection = db[collection_name]

    # Define the search filter using `$or` and `$regex`
    search_filter = {
        "$or": [
            {"article_name": {"$regex": keyword, "$options": "i"}},
            {"section_name": {"$regex": keyword, "$options": "i"}},
            {"article_para": {"$regex": keyword, "$options": "i"}},
            {"article_data.title": {"$regex": keyword, "$options": "i"}},
            {"article_data.article_para": {"$regex": keyword, "$options": "i"}},
            {"article_data.markdown_data": {"$regex": keyword, "$options": "i"}}
        ]
    }

    # Execute the query and return results (sorted by `created_at` field)
    searched_data = list(collection.find(search_filter).sort("created_at", -1))

    results = []

    for article in searched_data:
        # Extract the necessary fields based on the new design
        card = {
            "card_title": article.get("article_name", ""),
            "card_para": article.get("article_para", ""),
            "img_src": article.get("article_image", ""),
            "card_link": article.get("article_link", "")
        }
        results.append(card)

    return results


keyword = "test2"

make_index()

#print(search_articles(keyword))

print("--------------card-----data-----------")

#card_data = db_helper.get_card_data(DB_NAME, COLLECTION_NAME, "tech", 3)

#print(card_data)