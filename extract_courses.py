import os
import sys
import json
import pymongo
from bson.json_util import dumps

def main():
    try:
        connection = pymongo.MongoClient('mongodb://localhost:27017')
        database = connection.classroom
    except:
        connection = None

    if connection is not None:
        assignments = database.failed_submissions
        #courses = assignments.distinct('course')
        #print(courses)
        #for course in courses:
            #print(course)
        course_info = assignments.find({"guide.language.name":"haskell"})
            #with open('./'+ course.replace('/', '_') + '.json', 'w+') as jsonfile:
                #jsonfile.write(dumps(course_info))

    with open('./failed_submissions.json', 'w+') as jsonfile:
            jsonfile.write(dumps(course_info))
if __name__ == '__main__':
    main()
