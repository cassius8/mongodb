import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
scores = db.grades

def drop_HW():
	print("drop each students lowest homework")
	print(db.grades.count(), " total grades")
	pipeline=[{ "$unwind":"$scores" },{"$match":{"scores.type":"homework"}},{ "$group":{"_id":"$_id","minscore":{"$min":"$scores.score" }}} ]
	low_scores = scores.aggregate(pipeline)

	#scores.aggregate(pipeline)
	#hw_scores = scores.find( { 'type' : 'homework'}, { 'student_id' : 1, 'score' : 1, '_id' : 0}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)]).limit(10)
	#count=-1
	for result in low_scores:
		print(result)
	
		#print(result)
		#scores.update({'_id': result['_id']}, {"$pull":{"score": {"score":result["low_scores"]}}})
	
		

if __name__ == '__main__':
    drop_HW()
