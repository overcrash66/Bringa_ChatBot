from chatbot import app
from flask import render_template,current_app, flash, jsonify, make_response, redirect, request, url_for
from chatbot.forms import chatbotform
from chatbot.__init__ import model,words,classes,intents
import webbrowser
import nltk
import pickle
import json
import numpy as np
from keras.models import Sequential,load_model
import random
from datetime import datetime
import pytz
import requests
import os
import billboard
import time
from pygame import mixer
from operator import pow, truediv, mul, add, sub
import wikipedia
#nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from youtubesearchpython import *
from bs4 import BeautifulSoup
import re
lemmatizer=WordNetLemmatizer()

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

def get_response(return_list,intents_json,text):
	if len(return_list)==0:
		tag='noanswer' 
	else:
		tag=return_list[0]['intent']
	
	if tag=='datetime':
		x=''
		tz = pytz.timezone('Canada/Atlantic')
		dt=datetime.now(tz)
		x+=str(dt.strftime("%A"))+' '
		x+=str(dt.strftime("%d %B %Y"))+' '
		x+=str(dt.strftime("%H:%M:%S"))
		return x,'datetime'

	if tag=='weather':
		x=''
		url = "https://weatherapi-com.p.rapidapi.com/current.json"
		querystring = {"q":"canada moncton"}
		headers = {
			"X-RapidAPI-Key": "f783299ec7msh5bff4f5703a89b6p1329dfjsne38011da821f",
			"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
		}
		response = requests.request("GET", url, headers=headers, params=querystring) 
		response=response.json()
		pres_temp=response['current']['temp_c']
		feels_temp=response['current']['feelslike_c']
		x+='Current weather in Moncton New Brunswick Canada: Present temp.:'+str(pres_temp)+'C. Feels like:'+str(feels_temp)+'C. '
		print(x)
		return x,'weather'

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
			x+= " Source: "+'<a target="_blank" href="'+str(results[i][1])+'">' + str(results[i][1]) + "</a>"
			#x+=' '+(str(results[i][1]))
			if i!=9:
				x+='\n'

		return x,'news'
		
	if tag=='song':
		chart=billboard.ChartData('hot-100')
		x='The top 10 songs at the moment are: \n'
		for i in range(10):
			song=chart[i]
			x+=str(i+1)+'. '+str(song.title)+'- '+str(song.artist)
			if i!=9:
				x+='\n'
		return x,'songs'
		
	if tag=='google':
		from googlesearch import search as google
		query=text.split(':')[1].strip()
		query = query.replace(' ','+')
		for j in google(query, advanced=True, num_results=3,sleep_interval=1):
			j=(str(j))
		print('this is Last result: '+j)
		return j, 'google'
	
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
			results.append([ar["commence_time"],ar["home_team"],ar["away_team"],ar["scores"]])
		
		zz = len(results)
		for i in range(zz):
			x+=(str(i + 1))
			x+='. play time: '+str(results[i][0]+'')
			x+=' -'+(str(results[i][1])+'')
			x+=' Vs '+(str(results[i][2])+'')
			x+=' -Score: '+(str(results[i][3])+'')
			if i!=9:
				x+='\n'

		x=(str(x).replace('None','0'))
		print(str(x))
		return x,'soccer'

	
	if tag=='wikipedia':
		x=text.split(':')[1].strip()
		x = x.replace(' ','+')
		subject = x
		x=wikipedia.summary(subject)+'\n <a target="_blank" href="'+wikipedia.page(subject).url+'">'+wikipedia.page(subject).url+'</a>'
		return x,'wikipedia'
	
	if tag=="youtube":
		x=''
		query=text.split(':')[1].strip()
		query = query.replace(' ','+')
		customSearch = VideosSearch(query, limit = 10)
		for i in range(10):
			try:
				print(customSearch.result()['result'][i]['title'])
				print(customSearch.result()['result'][i]['link'])
				x+= (customSearch.result()['result'][i]['title'])
				origin = (customSearch.result()['result'][i]['link'])
				origin = origin.replace('watch?v=','embed/')
				x+= '<iframe width="420" height="315" frameborder="0" src="'+origin+'"></iframe>'+'\n'
			except Exception as inst:
				break
		return x,'youtube'
		
	if tag=="movie":
		x=''
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
				print(item['place']+ '-'+ item['movie_title']+ '('+item['year']+') -'+ 'Starring:'+ item['star_cast'])		
				x += (str(item['place'])+ '-'+ str(item['movie_title'])+ '('+str(item['year'])+') -'+'Starring:'+ str(item['star_cast'])+'\n')
		return x,'movie'
	
	if tag=="search":
		query=text.split(':')[1].strip()
		query = query.replace(' ','+')
		url = "http://api.duckduckgo.com/?q="+query+"&format=json"
		response = requests.request("GET", url) 
		response=response.json()
		x = response['Abstract']+" Source: "+'<a target="_blank" href="'+response['AbstractURL']+'">' + response['AbstractURL'] + "</a>"
		print(str(x))
		return x,'search'
	
	if tag=="calc":
		query=text.split(':')[1].strip()
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

		calc = query
		print("Answer: " + str(calculate(calc)))
		x = "Answer: " + str(calculate(calc))
		return x,'calc'
		
	if tag=='covid19':
		url = "https://corona.lmao.ninja/v2/countries/canada"
		response = requests.request("GET", url) 
		response=response.json()
		pres_temp=response['todayCases']
		feels_temp=response['todayDeaths']
		x='covid19: todayCases.:'+str(pres_temp)+'. todayDeaths:'+str(feels_temp)+'. '
		print(x)
		return x, 'covid19'
	
	list_of_intents= intents_json['intents']
	for i in list_of_intents:
		if tag==i['tag'] :
			result= random.choice(i['responses'])
	return result,tag

def response(text):
	return_list=predict_class(text,model)
	response,_=get_response(return_list,intents,text)
	return response
		

@app.route('/',methods=['GET','POST'])
def home():
	resp = make_response(render_template('index.html'))
	resp.set_cookie('username', expires=0)
	return resp
	#return render_template('index.html')

@app.route('/tag',methods=['GET','POST'])
def yo():
	resp = make_response(render_template('tag.html'))
	resp.set_cookie('username', expires=0)
	return resp
	#return render_template('tag.html')

@app.route("/get")
def chatbot():
	userText = request.args.get('msg')
	resp=response(userText)
	return resp

# @app.route('/tags.json',methods=['GET'])
# def JsonData():	 
	# # with open("tags.json", encoding='utf-8', errors='ignore') as json_d:
		# # tags = json.load(json_d, strict=False)
	# resp = make_response(render_template('tags.json'))
	# resp.set_cookie('username', expires=0)
	# return resp	 
	# #return render_template('tags.json', tags = tags)	   