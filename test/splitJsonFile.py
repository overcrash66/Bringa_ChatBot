#import sys
import json
#import re
# f = open('exportedFile.json', 'w')
# with open("Baseintents.json", "r",encoding="utf8") as read_file:
    # for c in read_file:
        # c = c.replace("\'", "\"")
        # c = c.replace("\n", "")
        # c = c.replace("'", '"')
        # f.write(c)
    # f.close()

'''studentsList = []
print("Started Reading JSON file which contains multiple JSON document")
with open('exportedFile.json') as f:
    for jsonObj in f:
        studentDict = json.loads(jsonObj)
        studentsList.append(studentDict)

print("Printing each JSON Decoded Object")
for student in studentsList:
    print(student["intents"])'''
     
splitLen = 4200
outputBase = 'intents'
   
data = open('intents.json', 'r')

count = 0
at = 0
dest = None

for line in data:
    #print("create Json")
    if count % splitLen == 0:
        if dest: dest.close()
        dest = open(outputBase + str(at) + '.json', 'w')
        at += 1
    dest.write(line)
    count += 1
dest.close()