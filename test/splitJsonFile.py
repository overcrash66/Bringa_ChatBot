import json
	 
splitLen = 4200
outputBase = 'intents'
   
data = open('intents.json', 'r')

count = 0
at = 0
dest = None

for line in data:
	if count % splitLen == 0:
		if dest: dest.close()
		dest = open(outputBase + str(at) + '.json', 'w')
		at += 1
	dest.write(line)
	count += 1
dest.close()