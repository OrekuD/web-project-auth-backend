from pymongo import MongoClient

db_client = MongoClient("mongodb+srv://orekud:HU2nQNrQ0twKWqjx@cluster0.yf8wbob.mongodb.net/?retryWrites=true&w=majority") 

db = db_client.license_detection