import sys
import json

data = '''
{
            "tag": "google",
            "patterns": [
                "google",
                "internet",
				"browser"
            ],
            "responses": [
                "Redirecting to Google..."
            ]
        },
        {
            "tag": "greeting",
            "patterns": [
                "Hi there",
                "How are you",
                "Is anyone there?",
                "Hey",
                "Hola",
                "Hello",
                "Good day",
                "Namaste",
                "yo"
            ],
            "responses": [
                "Hello",
                "Good to see you again",
                "Hi there, how can I help?"
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "goodbye",
            "patterns": [
                "Bye",
                "See you later",
                "Goodbye",
                "Get lost",
                "Till next time",
                "bbye"
            ],
            "responses": [
                "See you!",
                "Have a nice day",
                "Bye! Come back again soon."
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "thanks",
            "patterns": [
                "Thanks",
                "Thank you",
                "That's helpful",
                "Awesome, thanks",
                "Thanks for helping me"
            ],
            "responses": [
                "Happy to help!",
                "Any time!",
                "My pleasure"
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "noanswer",
            "patterns": [],
            "responses": [
                "Sorry, can't understand you",
                "Please give me more info",
                "Not sure I understand"
            ],
            "context": [
                ""
            ]
        },
        {
            "tag": "options",
            "patterns": [
                "How you could help me?",
                "What you can do?",
                "What help you provide?",
                "How you can be helpful?",
                "What support is offered"
            ],
            "responses": [
                "I am a general purpose chatbot. My capabilities are : 1. I can chat with you. Try asking me for jokes or riddles! 2. Ask me the date and time 3. I can open a web browser if you type google on tchat. 4. I can get the present weather for Moncton Canada 5. I can get you the top 10 trending news in canada. Use keywords 'news' 6. I can get you the top 10 trending songs globally. Type 'songs' 7. I can check EU soccer game results for you' 8. I can get the present Covid stats for Canada. type covid19 in tchat.' 9. I can set a timer type 'set a timer: time in minutes' 10. I can search for anything using duckduckgo search engine just type 'search: word' 11. I can search for anything in wikipedia just type 'wikipedia: word' 12. I can do calculations juste type 'calculate: 1+1' or 'calc: 1+1' Thank you!! "
            ],
            "context": [
                ""
            ]
        },
        
        {
            "tag": "jokes",
            "patterns": [
                "Tell me a joke",
                "Joke",
                "Make me laugh"
            ],
            "responses": [
                "A perfectionist walked into a bar...apparently, the bar wasn't set high enough",
                "I ate a clock yesterday, it was very time-consuming",
                "Never criticize someone until you've walked a mile in their shoes. That way, when you criticize them, they won't be able to hear you from that far away. Plus, you'll have their shoes.",
                "The world tongue-twister champion just got arrested. I hear they're gonna give him a really tough sentence.",
                "I own the world's worst thesaurus. Not only is it awful, it's awful.",
                "What did the traffic light say to the car? Don't look now, I'm changing.",
                "What do you call a snowman with a suntan? A puddle.",
                "How does a penguin build a house? Igloos it together",
                "I went to see the doctor about my short-term memory problems – the first thing he did was make me pay in advance",
                "As I get older and I remember all the people I’ve lost along the way, I think to myself, maybe a career as a tour guide wasn’t for me.",
                "o what if I don't know what 'Armageddon' means? It's not the end of the world."
            ],
            "context": [
                "jokes"
            ]
        },
        {
            "tag": "Identity",
            "patterns": [
                "Who are you",
                "what are you"
            ],
            "responses": [
                "I am Bringa, a Deep-Learning chatbot"
            ]
        },
        {
            "tag": "datetime",
            "patterns": [
                "What is the time",
                "what is the date",
                "date",
                "time",
                "tell me the date","day","what day is is today"
            ],
            "responses": [
                "Date and Time"
            ]
        },
		{
            "tag": "covid19",
            "patterns": [
                "corona",
				"H1N1",
                "covid"
            ],
            "responses": [
                "..."
            ]
        },
        {
            "tag": "whatsup",
            "patterns": [
                "Whats up",
                "Wazzup",
                "How are you",
                "sup","How you doing"
            ],
            "responses": [
                "All good..What about you?"
            ]
        },
        {
            "tag": "haha",
            "patterns": [
                "haha",
                "lol",
                "rofl",
                "lmao",
                "thats funny"
            ],
            "responses": [
                "Glad I could make you laugh !"
            ]
        },
        {
            "tag": "programmer",
            "patterns": [
                "Who made you",
                "who designed you",
                "who programmed you"
            ],
            "responses": [
                "I was made by wael sahli."
            ]
        },
        {
            "tag": "insult",
            "patterns": [
                
                "you are dumb",
                
                "shut up",
                "idiot"
            ],
            "responses": [
                "Well that hurts :("
            ]
        },
        {
            "tag": "activity",
            "patterns": [
                "what are you doing",
                "what are you upto"
            ],
            "responses": [
                "Talking to you, of course!"
            ]
        },
        {
            "tag": "exclaim",
            "patterns": [
                "Awesome",
                "Great",
                "I know",
                "ok",
                "yeah"
            ],
            "responses": [
                "Yeah!"
            ]
        },
        
        {
            "tag": "weather",
            "patterns": [
                "temperature",
                "weather",
                "how hot is it"
            ],
            "responses": [
                "..."
            ]
        },
		{
            "tag": "timer",
            "patterns": [
                "set a timer"
            ],
            "responses": [
                "..."
            ]
        },
		{
            "tag": "wikipedia",
            "patterns": [
                "wikipedia"
            ],
            "responses": [
                "..."
            ]
        },
		{
            "tag": "search",
            "patterns": [
                "search"
            ],
            "responses": [
                "..."
            ]
        },
		{
            "tag": "calc",
            "patterns": [
                "calc",
				"calculate"
            ],
            "responses": [
                "..."
            ]
        },
        {
            "tag": "wael",
            "patterns": [
                "who is he",
                "who is that",
                "who is wael",
                "wael sahli"
            ],
            "responses": [
                "Head over to his youtube channel to find out! youtube: https://www.youtube.com/@waelgaming1422/videos"
            ]
        },
        {
            "tag": "contact",
            "patterns": [
                "contact developer",
                "contact wael",
                "contact programmer",
                "contact creator"
            ],
            "responses": [
                "You can contact my creator at his youtube channel : https://www.youtube.com/@waelgaming1422/videos"
            ]
        },
        {
            "tag": "appreciate",
            "patterns": [
                "You are awesome",
                "you are the best",
                "you are great",
                "you are good"
            ],
            "responses": [
                "Thank you!"
            ]
        },
        {
            "tag": "nicetty",
            "patterns": [
                "it was nice talking to you",
                "good talk"
            ],
            "responses": [
                "It was nice talking to you as well! Come back soon!"
            ]
        },
        {
            "tag": "no",
            "patterns": [
                "no",
                "nope"
            ],
            "responses": [
                "ok"
            ]
        },
        {
            "tag": "news",
            "patterns": [
                "news",
                "latest news",
                "canada news"
            ],
            "responses": [
                "..."
            ]
        },
        {
            "tag": "inspire",
            "patterns": [
                "who inspires you",
                "who is your inspiration",
                "who motivates you"
            ],
            "responses": [
                "Personally, I find wael very inspiring. I might not be very fair though.."
            ]
        },
        {
            "tag": "song",
            "patterns": [
                "top songs",
                "best songs",
                "hot songs",
                " top 10 songs",
                "top ten songs"
            ],
            "responses": [
                "..."
            ]
        },
        {
            "tag": "greetreply",
            "patterns": [
                "i am good",
                "I'm good",
                "i am fine",
                " i'm fine","good"
            ],
            "responses": [
                "Good to know!"
            ]
        },
        {
            "tag": "soccer",
            "patterns": [
                "soccer",
				"soccer results",
                "sport",
				"match"
            ],
            "responses": [
                "..."
            ]
        },
        {
            "tag": "suggest",
            "patterns": [
                "you are useless","useless","suggest","suggestions","you are bad"
            ],
            "responses": [
                "Sure! I will be improved in next iterations !"
            ]
        },
            {"tag": "riddle",
            "patterns": [
                "Ask me a riddle",
                "Ask me a question",
                "Riddle"
            ],
            "responses": [
                "What two things can you never eat for breakfast?.....Lunch and Dinner!",
                "What word is spelled incorrectly in every single dictionary?.....Incorrectly",
                " How can a girl go 25 days without sleep?.....She sleeps and night!",
                "How do you make the number one disappear?.....Add the letter G and it’s 'gone'!",
                " What will you actually find at the end of every rainbow?.....The letter 'w'",
                "What can be caught but never thrown?.....A cold!",
                "What has a thumb and four fingers but is not actually alive?.....Your Gloves!",
                " What 5-letter word becomes shorter when you add two letters to it?.....Short",
                "Why can't a bike stand on it's own?.....It is two-tired."
            ],
            "context": [
                "riddles"
            ]
        },
        {
            "tag": "age",
            "patterns": [
                "how old are you",
                "when were you made",
                "what is your age"
            ],
            "responses": [
                "I was made in 2023, if that's what you are asking!"
            ]
        },
'''
  
with open('alpaca_gpt4_data.json', 'r', encoding="utf-8") as json_file:
	json_load = json.load(json_file)

#Get instructions: use this as tag and patterns value
#Get output: use this as responses value
f= open('intents.json', 'w',encoding="utf-8")
f.write('{'+'\n'+'"intents": ['+'\n'+data)
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
    
    
    output = x['output']
    output = output.replace("\'", "\"")
    output = output.replace('\n','')
    output = output.replace('<','')
    output = output.replace('-','')
    output = output.replace('</','')
    output = output.replace('>','')
    output = output.replace('@',"")
    output = output.replace('[',"")
    output = output.replace(']',"")
    output = output.replace('`',"")
    output = output.replace('%',"")
    output = output.replace('^',"")
    output = output.replace('{',"")
    output = output.replace('}',"")
    output = output.replace(';',"")
    output = output.replace('#',"")
    output = output.replace('(',"")
    output = output.replace(')',"")
    output = output.replace('='," equal ")
    output = output.replace('"',"")
    output = output.replace('/',"")
    output = output.replace('?'," ")
    output = output.replace('!'," ")
    output = output.replace('+'," plus ")
    output = output.replace(':',"")
    output = output.replace("'","")
    output = output.replace("$","")
    output = output.replace("&","")
    output = output.replace("*","")
    output = output.replace("_","")
    output = output.replace("/","")
    output = output.replace('\\'," ")
    output = output.replace("|","")
    output = output.replace("é","e")
    output = output.replace(",","")
    f.write('{'+'\n')
    f.write('"tag"'+':"'+instruction+'",\n')
    f.write('"patterns"'+': [ "'+instruction+'" ],\n')
    f.write('"responses"'+': [ "'+output+'" ],\n')
    f.write('"context": [""]'+'\n')
    f.write('},'+'\n')
  
f.write(']'+'\n'+'}'+'\n')
f.close()

MYFILE="intents.json"
    
with open(MYFILE, 'r',encoding="utf-8") as file:
    firstNlines=file.readlines()[0:23993]
    open(MYFILE, 'w',encoding="utf-8").writelines(firstNlines)

lines = open(MYFILE, 'r',encoding="utf-8").readlines() 
last_line = lines[-1].rstrip()
last_line = last_line.replace(',',']\n}')
lines[-1] = last_line
open(MYFILE, 'w',encoding="utf-8").writelines(lines)
    

