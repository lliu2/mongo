from pymongo import MongoClient

server = MongoClient("lisa.stuy.edu")
ourDB = server['bagels']

def getAvg(studentID):
    studentDoc = ourDB.students.find_one( {"id": studentID} );
    courses = studentDoc["courses"] #list of dicts
    total = 0;
    for course in courses: #course is a dict { code: ___, mark: ___ }
        total += int( course['mark'] )
    return total * 1.0 / len(courses)

def printAllAvgs():
    docs = ourDB.students.find()
    for doc in docs:
        print "name: ", doc['name'], "\tid: ", doc['id'], "\taverage: ", getAvg( doc['id'] )

def updateStudentAge(studentID, newAge):
    students = ourDB.students.find()
    ourDB.students.update_one({"id" : studentID}, { "$set": { "age" : newAge }})
    return true
