from pymongo import MongoClient

db_client = MongoClient("mongodb+srv://orekud:HU2nQNrQ0twKWqjx@cluster0.l490dq4.mongodb.net/?retryWrites=true&w=majority") 

db = db_client.license_detection