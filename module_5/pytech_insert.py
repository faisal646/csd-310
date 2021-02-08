"""
    Title: pytech_insert.py
    Author: Salahauddin Faisal
    Date: 04 February 2021
    Description: Program for inserting data into connected collections
"""

import pymongo
from pymongo import MongoClient

# Connecting to MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.o4awn.mongodb.net/students?retryWrites=true&w=majority"
client = MongoClient(url)
# Linking Database with client object
db = client.pytech
students = db.students

# thorin = {
#     "First Name": "Thorin",
#     "Last Name": "Oakenshield"
# }

# bilbo = {
#     "First Name": "Bilbo",
#     "Last Name": "Baggins"
# }

# frodo = {
#     "First Name": "Frodo",
#     "Last Name": "Baggins"
# }

# print("\n  -- INSERT STATEMENTS --")

# thorin_student_id = students.insert_one(thorin).inserted_id
# print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))
# bilbo_student_id = students.insert_one(bilbo).inserted_id
# print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))
# frodo_student_id = students.insert_one(frodo).inserted_id
# print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))


Thorin = {
    "_id": "1007",
    "First Name": "Thorin",
    "Last Name": "Oakenshield",
    "enrollments":[
        {
        "term": "summer",
        "gpa": "4.6",
        "start_date":"12/12/22",
        "end_date": "12/11/22",
        "courses": [
            {
            "course_id":"006",
            "description":"english006",
            "instructor":"Mr. Smith",
            "grade": "AAA"
            },
            {
            "course_id":"009",
            "description":"french009",
            "instructor":"Mr. Joe",
            "grade": "AAA"
            },
        ]
        }
    ]
}

Bilbo = {
    "_id": "1008",
    "First Name": "Bilbo",
    "Last Name": "Baggins",
    "enrollments":[
        {
        "term": "summer",
        "gpa": "4.5",
        "start_date":"12/12/22",
        "end_date": "12/11/22",
        "courses": [
            {
            "course_id":"007",
            "description":"english007",
            "instructor":"mr john",
            "grade": "AAA"
            },
            {
            "course_id":"008",
            "description":"french008",
            "instructor":"mr jean",
            "grade": "AAA"
            },
        ]
        }
    ]
}

Frodo = {
    "_id": "1009",
    "First Name": "Frodo",
    "Last Name": "Baggins",
    "enrollments":[
        {
        "term": "summer",
        "gpa": "4.4",
        "start_date":"12/12/22",
        "end_date": "12/11/22",
        "courses": [
            {
            "course_id":"070",
            "description":"Physics-070",
            "instructor":"Mr. Will",
            "grade": "AAA"
            },
            {
            "course_id":"008",
            "description":"French-008",
            "instructor":"Mr. Erik",
            "grade": "AAA"
            },
        ]
        }
    ]
}

try:
    students.insert_one(Thorin)
except Exception as e:
    #print(e)
    pass
    
try:
    students.insert_one(Bilbo)
except pymongo.errors.DuplicateKeyError:
    pass

try:
    students.insert_one(Frodo)
except pymongo.errors.DuplicateKeyError:
    pass   
