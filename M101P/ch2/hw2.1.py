import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.students
scores = db.grades

def drop_HW():
	print("drop each students lowest homework")
	print(db.grades.count(), " total grades!")
	low_score = []
	pipeline=[{'$match':{'type':'homework'}},{'$group':{'_id':'$student_id', 'minimum':{'$min':'$score'}}}]
	low_score = db.grades.aggregate(pipeline)
	for score in low_score:
		print(score)

	#hwscores = scores.find({'type':'homework'},)
	#print(scores.find_one({'type':'homework'}))

	"""query = {'type': 'exam'}
    projection = {'student_id': 1, '_id': 0}
    cursor = scores.find(query, projection)
    print(cursor)"""
    
    

	#query = {'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1}
	#query2 = 
	

if __name__ == '__main__':
    drop_HW()
