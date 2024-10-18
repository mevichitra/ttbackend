import os
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')

# Specify the database name directly
database_name = "ttdb"

# Create the MongoClient with the certifi CA bundle
client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())
db = client[database_name]
