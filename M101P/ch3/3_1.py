# Andrew Erlichson
# MongoDB, Inc. 
# M101P - Copyright 2015, All Rights Reserved



import pymongo

conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.school
students = db.students

for student_data in students.find():
    smaller_homework_score_seq = None
    smaller_homework_score_val = None
    for score_seq, score_data in enumerate(student_data['scores']):
        if score_data['type'] == 'homework':
            if smaller_homework_score_seq is None or smaller_homework_score_val > score_data['score']:
                smaller_homework_score_seq = score_seq
                smaller_homework_score_val = score_data['score']
    students.update({'_id': student_data['_id']}, {'$pop': {'scores': smaller_homework_score_seq}})
"""
# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
db=connection.school
scores = db.students
#print (scores.find_one({"scores.type":"homework"}))        
pipeline=[{"$unwind":'$scores'},
{ "$group": {"_id" : "1",'scores.type': 'homework'}}]
#{ "$sort": {'scores.score': 1}}
cursor = scores.aggregate(pipeline)
	
#cursor = scores.find().sort("scores.score",pymongo.ASCENDING)
#cursor = scores.find_one()
print(cursor)
# removes one student
def remove_student(student_id):
	#takes the student_id and locates the lowest homework score and removes it
	pass
def find_student():
	db=connection.school
	scores = db.students
	print (scores.find_one())
	try: 
		docs = scores.find_one()
		print docs
		for doc in docs:
			print (doc)

	except Exception as e:
		print ("Exception: ", type(e), e)

#find_student()"""