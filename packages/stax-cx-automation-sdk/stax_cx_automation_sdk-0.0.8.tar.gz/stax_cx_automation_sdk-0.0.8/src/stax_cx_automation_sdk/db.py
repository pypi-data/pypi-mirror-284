from pymongo import MongoClient
import os

db = MongoClient(os.getenv('DB_URI', default="mongodb+srv://api:rCFojHAbs0o8MouH@cx-db.pewoo.mongodb.net/db"))[os.getenv('DB_NAME', default="db")]