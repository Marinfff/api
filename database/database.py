from pymongo import MongoClient
from config.db import URL

server = MongoClient(URL)
db = server.test
collection = db.users
