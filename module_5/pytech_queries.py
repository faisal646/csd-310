"""
    Title: pytech_queries.py
    Author: Salahauddin Faisal
    Date: 07 February 2021
    Document: Program to make queries on the connected Database Collections
 """

import pymongo
from pymongo import MongoClient

# Connecting to MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.o4awn.mongodb.net/students?retryWrites=true&w=majority"
client = MongoClient(url)
# Linking Database with client object
db = client.pytech
students = db.students

# # MongoDB: find() Example
# docs = db.students.find({})
# for doc in docs:
#     print (doc)
#     print("\n")

# # MongoDB: find_one() Example
# doc = db.students.find_one({"_id": "1008"})
# print(doc["_id"])

print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

docs = db.students.find({})
for doc in docs:
    print("Student ID:", doc["_id"])
    print("First Name:", doc["First Name"])
    print("Last Name:", doc["Last Name"])
    print()

print("\n-- DISPLAYING STUDENTS DOCUMENT FROM find_one() QUERY -- ")
student_1008 = db.students.find_one({"_id": "1008"})
print("Student ID:", student_1008["_id"])
print("First Name:", student_1008["First Name"])
print("Last Name:", student_1008["Last Name"])

print("\nEnd of program, press any key to continue...\n")