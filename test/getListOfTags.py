import sys
import json
data = '''
{
            "tag": "google"
        },
        {
            "tag": "greeting"
        },
        {
            "tag": "goodbye"
        },
        {
            "tag": "thanks"
        },
        {
            "tag": "noanswer"
        },
        {
            "tag": "options"
        },
        {
            "tag": "jokes"
        },
        {
            "tag": "Identity"
        },
        {
            "tag": "datetime"
        },
		{
            "tag": "covid19"
        },
        {
            "tag": "whatsup"
        },
        {
            "tag": "haha"
        },
        {
            "tag": "programmer"
        },
        {
            "tag": "insult"
        },
        {
            "tag": "activity"
        },
        {
            "tag": "exclaim"
        },
        
        {
            "tag": "weather"
        },
		{
            "tag": "timer"
        },
		{
            "tag": "wikipedia"
        },
		{
            "tag": "search"
        },
		{
            "tag": "calc"
        },
        {
            "tag": "wael"
        },
        {
            "tag": "contact"
        },
        {
            "tag": "appreciate"
        },
        {
            "tag": "nicetty"
        },
        {
            "tag": "no"
        },
        {
            "tag": "news"
        },
        {
            "tag": "inspire"
        },
        {
            "tag": "song"
        },
        {
            "tag": "greetreply"
        },
        {
            "tag": "soccer",
        },
        {
            "tag": "suggest"
        },
            {"tag": "riddle"
        },
        {
            "tag": "age"
        },
'''

with open('alpaca_gpt4_data.json', 'r', encoding="utf-8") as json_file:
	json_load = json.load(json_file)

f= open('tags.json', 'w',encoding="utf-8")
f.write('{'+'\n'+'"tags": ['+'\n'+data)
for x in json_load:
    instruction = x['instruction']
    instruction = instruction.replace("\'", "\"")
    instruction = instruction.replace('"',"'")
    instruction = instruction.replace('\n','')
    instruction = instruction.replace('<','')
    instruction = instruction.replace('</','')
    instruction = instruction.replace('>','')
    instruction = instruction.replace('@',"at")
    instruction = instruction.replace('[',"")
    instruction = instruction.replace(']',"")
    instruction = instruction.replace('`',"")
    instruction = instruction.replace('%'," ")
    instruction = instruction.replace('^',"")
    instruction = instruction.replace('{',"")
    instruction = instruction.replace('}',"")
    instruction = instruction.replace(';',"")
    instruction = instruction.replace('#',"")
    instruction = instruction.replace('(',"")
    instruction = instruction.replace(')',"")
    instruction = instruction.replace('='," equal ")
    instruction = instruction.replace('"',"")
    instruction = instruction.replace('/',"")
    instruction = instruction.replace('?',"")
    instruction = instruction.replace('!',"")
    instruction = instruction.replace('-',"")
    instruction = instruction.replace('+'," plus ")
    instruction = instruction.replace(':',"")
    instruction = instruction.replace("'","")
    instruction = instruction.replace("$","")
    instruction = instruction.replace("&","")
    instruction = instruction.replace("*","")
    instruction = instruction.replace("_","")
    instruction = instruction.replace("/","")
    instruction = instruction.replace('\\',"")
    instruction = instruction.replace("|","")
    instruction = instruction.replace("é","e")
    instruction = instruction.replace(",","")
    
    f.write('{'+'\n')
    f.write('"tag"'+':"'+instruction+'"\n')
    f.write('},'+'\n')
  
f.write(']'+'\n'+'}'+'\n')
f.close()

MYFILE="tags.json"
    
with open(MYFILE, 'r',encoding="utf-8") as file:
    firstNlines=file.readlines()[0:11703]
    open(MYFILE, 'w',encoding="utf-8").writelines(firstNlines)

lines = open(MYFILE, 'r',encoding="utf-8").readlines() 
last_line = lines[-1].rstrip()
last_line = last_line.replace(',',']\n}')
lines[-1] = last_line
open(MYFILE, 'w',encoding="utf-8").writelines(lines)