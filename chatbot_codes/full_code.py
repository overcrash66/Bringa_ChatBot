import sys
import wikipedia
import keras
import nltk
import pickle
import json
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation
import random
import datetime
from googlesearch import search
import webbrowser
import requests
import billboard
import time
from pygame import mixer
from json import JSONDecodeError
from operator import pow, truediv, mul, add, sub 
from nltk.stem import WordNetLemmatizer
from youtubesearchpython import *
from bs4 import BeautifulSoup
import re
lemmatizer=WordNetLemmatizer()

words=[]
classes=[]
documents=[]
ignore=['?','!',',',"'s"]
   
with open("intents.json", encoding='utf-8', errors='ignore') as json_data:
	 intents = json.load(json_data, strict=False)

for intent in intents['intents']:
	for pattern in intent['patterns']:
		w=nltk.word_tokenize(pattern)
		words.extend(w)
		documents.append((w,intent['tag']))
		
		if intent['tag'] not in classes:
			classes.append(intent['tag'])
			
words=[lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore]
words=sorted(list(set(words)))
classes=sorted(list(set(classes)))
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

#training data
training=[]
output_empty=[0]*len(classes)

for doc in documents:
	bag=[]
	pattern=doc[0]
	pattern=[ lemmatizer.lemmatize(word.lower()) for word in pattern ]
	
	for word in words:
		if word in pattern:
			bag.append(1)
		else:
			bag.append(0)
	output_row=list(output_empty)
	output_row[classes.index(doc[1])]=1
	
	training.append([bag,output_row])
	
random.shuffle(training)
training=np.array(training)	 
X_train=list(training[:,0])
y_train=list(training[:,1])	 

#Model
model=Sequential()
model.add(Dense(128,activation='relu',input_shape=(len(X_train[0]),)))
model.add(Dropout(0.5))
model.add(Dense(64,activation='relu'))
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(y_train[0]),activation='softmax'))

adam=keras.optimizers.Adam(0.001)
model.compile(optimizer=adam,loss='categorical_crossentropy',metrics=['accuracy'])
#model.fit(np.array(X_train),np.array(y_train),epochs=200,batch_size=10,verbose=1)
# !!!!! Enable training mode here !!!!!
weights=model.fit(np.array(X_train),np.array(y_train),epochs=200,batch_size=10,verbose=1)	 
model.save('mymodel.h5',weights)

from keras.models import load_model
model = load_model('mymodel.h5')
 
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

#Predict
def clean_up(sentence):
	sentence_words=nltk.word_tokenize(sentence)
	sentence_words=[ lemmatizer.lemmatize(word.lower()) for word in sentence_words]
	return sentence_words

def create_bow(sentence,words):
	sentence_words=clean_up(sentence)
	bag=list(np.zeros(len(words)))
	
	for s in sentence_words:
		for i,w in enumerate(words):
			if w == s: 
				bag[i] = 1
	return np.array(bag)

def predict_class(sentence,model):
	p=create_bow(sentence,words)
	res=model.predict(np.array([p]))[0]
	threshold=0.8
	results=[[i,r] for i,r in enumerate(res) if r>threshold]
	results.sort(key=lambda x: x[1],reverse=True)
	return_list=[]
	
	for result in results:
		return_list.append({'intent':classes[result[0]],'prob':str(result[1])})
	return return_list

def get_response(return_list,intents_json):
	
	if len(return_list)==0:
		tag='noanswer'
	else:	 
		tag=return_list[0]['intent']
	
	if tag=='datetime':		   
		print(time.strftime("%A"))
		print (time.strftime("%d %B %Y"))
		print (time.strftime("%H:%M:%S"))

	if tag=='google':
		x=input('inter your google search here: ')
		query = x
		for j in search(query, advanced=True, num_results=3,sleep_interval=1):
			print(j)
		return j, 'google'
		
	if tag=='weather':
		url = "https://weatherapi-com.p.rapidapi.com/current.json"
		querystring = {"q":"canada moncton"}
		headers = {
			"X-RapidAPI-Key": "f783299ec7msh5bff4f5703a89b6p1329dfjsne38011da821f",
			"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
		}
		response = requests.request("GET", url, headers=headers, params=querystring) 
		x=response.json()
		print("Current weather in Moncton New Brunswick Canada: ")
		print('Present temp.: ',x['current']['temp_c'],'celcius ')
		print('Feels Like:: ',x['current']['feelslike_c'],'celcius ')
		
	if tag=='news':
		main_url = " http://newsapi.org/v2/top-headlines?country=ca&apiKey=bc88c2e1ddd440d1be2cb0788d027ae2"
		open_news_page = requests.get(main_url).json()
		article = open_news_page["articles"]
		results = []
		x=''
		for ar in article:
			results.append([ar["title"],ar["url"]])

		for i in range(10):
			x+=(str(i + 1))
			x+='. '+str(results[i][0])
			x+=(str(results[i][1]))
			if i!=9:
				x+='\n'

		return x,'news'
			
	if tag=='soccer':
		x=''
		url = "https://odds.p.rapidapi.com/v4/sports/soccer_uefa_champs_league/scores"
		querystring = {"daysFrom":"3"}
		headers = {
			"X-RapidAPI-Key": "f783299ec7msh5bff4f5703a89b6p1329dfjsne38011da821f",
			"X-RapidAPI-Host": "odds.p.rapidapi.com"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		response=response.json()

		results = []

		for ar in response:
			results.append([ar["home_team"],ar["away_team"],ar["scores"]])

		for i in range(4):
			x+=(str(i + 1))
			x+='. '+str(results[i][0]+'')
			x+=' Vs '+(str(results[i][1])+'')
			x+=' -Score: '+(str(results[i][2])+'')
			if i!=9:
				x+='\n'

		x=(str(x).replace('None','0'))
		#print(str(x))
		return x,'soccer'
		
	if tag=='song':
		chart=billboard.ChartData('hot-100')
		print('The top 10 songs at the moment are:')
		for i in range(10):
			song=chart[i]
			print(song.title,'- ',song.artist)
		
	if tag=='youtube':
		query = input("Enter Your Search Here: ")
		query = query.replace(' ','+')
		customSearch = VideosSearch(query, limit = 10)
		for i in range(10):
			try:
				print(customSearch.result()['result'][i]['title'])
				print(customSearch.result()['result'][i]['link'])
			except Exception as inst:
				break
	
	if tag=='movie':
		url = 'http://www.imdb.com/chart/top'
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')

		movies = soup.select('td.titleColumn')
		links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
		crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
		ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
		votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

		imdb = []

		# Store each item into dictionary (data), then put those into a list (imdb)
		for index in range(0, len(movies)):
			# Seperate movie into: 'place', 'title', 'year'
			movie_string = movies[index].get_text()
			movie = (' '.join(movie_string.split()).replace('.', ''))
			movie_title = movie[len(str(index))+1:-7]
			year = re.search('\((.*?)\)', movie_string).group(1)
			place = movie[:len(str(index))-(len(movie))]
			data = {"movie_title": movie_title,
					"year": year,
					"place": place,
					"star_cast": crew[index],
					"rating": ratings[index],
					"vote": votes[index],
					"link": links[index]}
			imdb.append(data)
		# i=0
		for item in imdb:
			gg = item['year']
			gg = gg.replace('(','')
			gg = gg.replace(')','')
			if gg > '2020':
				print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast']) 
	
	if tag=='wikipedia':
		x=input('inter your search here: ')
		subject = x
		print("\n"+wikipedia.summary(subject))
		print(wikipedia.page(subject).url)
	
	if tag=="search":
		query=input('inter your search here: ')
		url = "http://api.duckduckgo.com/?q="+query+"&format=json"
		response = requests.request("GET", url) 
		response=response.json()
		x = response['Abstract']+" Source: "+response['AbstractURL']
		print(str(x))
		return x,'search'
		
	if tag=="calc":
		operators = {
		  '+': add,
		  '-': sub,
		  '*': mul,
		  '/': truediv
		}

		def calculate(s):
			if s.isdigit():
				return float(s)
			for c in operators.keys():
				left, operator, right = s.partition(c)
				if operator in operators:
					return operators[operator](calculate(left), calculate(right))

		calc = input("Type calculation:\n")
		print("Answer: " + str(calculate(calc)))
		
	if tag=='covid19':
		url = "https://corona.lmao.ninja/v2/countries/canada"
		response = requests.request("GET", url) 
		response=response.json()
		pres_temp=response['todayCases']
		feels_temp=response['todayDeaths']
		x='covid19: todayCases.:'+str(pres_temp)+'. todayDeaths:'+str(feels_temp)+'. '
		print(x)
		return x,'covid19'

	list_of_intents= intents_json['intents']	
	for i in list_of_intents:
		if tag==i['tag'] :
			result= random.choice(i['responses'])
	return result

def response(text):
	return_list=predict_class(text,model)
	response=get_response(return_list,intents)
	return response

while(1):
	x=input()
	print(response(x))
	if x.lower() in ['bye','goodbye','get lost','see you']:	 
		break


#Self learning
# print('Help me Learn?')
# tag=input('Please enter general category of your question	 ')
# flag=-1
# for i in range(len(intents['intents'])):
	# if tag.lower() in intents['intents'][i]['tag']:
		# intents['intents'][i]['patterns'].append(input('Enter your message: '))
		# intents['intents'][i]['responses'].append(input('Enter expected reply: '))		  
		# flag=1

# if flag==-1:
	
	# intents['intents'].append (
		# {'tag':tag,
		 # 'patterns': [input('Please enter your message')],
		 # 'responses': [input('Enter expected reply')]})
	
# with open('intents.json','w') as outfile:
	# outfile.write(json.dumps(intents,indent=4))