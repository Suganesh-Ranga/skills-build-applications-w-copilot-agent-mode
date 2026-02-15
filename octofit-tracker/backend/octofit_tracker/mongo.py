from pymongo import MongoClient
from django.conf import settings

# Utility to get MongoDB client and database
def get_mongo_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['octofit_db']
    return db
