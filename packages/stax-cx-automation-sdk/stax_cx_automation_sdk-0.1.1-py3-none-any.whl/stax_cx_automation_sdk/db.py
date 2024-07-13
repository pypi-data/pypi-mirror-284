from pymongo import MongoClient
from os import getenv

db = MongoClient(getenv('DB_URI', default="mongodb+srv://api:rCFojHAbs0o8MouH@cx-db.pewoo.mongodb.net/db")).get_database(getenv('DB_NAME', default='db'))