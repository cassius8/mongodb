import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
scores = db.grades

def drop_HW():
	students = db.students
	cursor = students.find({})
	for doc in cursor:
	        hw_scores = []
	        for item in doc["scores"]:
	            if item["type"] == "homework":
	                hw_scores.append(item["score"])
	        hw_scores.sort()
	        print(doc)
	        hw_min = hw_scores[0]
	        students.update({"_id": doc["_id"]},
	                        {"$pull":{"scores":{"score":hw_min}}})


if __name__ == '__main__':
    drop_HW()	