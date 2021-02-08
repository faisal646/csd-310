"""
    Title: pytech_test.py
    Author: Salahauddin Faisal
    Date: 04 February 2021
    Document: Test program for the listings of connected collections
"""

# This program shows the connected collections 
import pymongo
from pymongo import MongoClient

# Connecting to MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.o4awn.mongodb.net/students?retryWrites=true&w=majority"
client = MongoClient(url)

# Linking Database with client object
db = client.pytech

print("\n -- Pytech Collection List --\n")
print(db.list_collection_names())
print("\n -- End of Program --")






