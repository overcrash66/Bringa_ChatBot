import flask
from flask import Flask
from chatbotconfig import Config

app=Flask(__name__)
app.config.from_object(Config)

import keras
import nltk
import pickle
import json
from keras.models import load_model

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

model=load_model('chatbot_codes/mymodel.h5')
# intents = json.loads(open('chatbot_codes/intents.json').read())
with open("chatbot_codes/intents.json", encoding='utf-8', errors='ignore') as json_data:
     intents = json.load(json_data, strict=False) 
words = pickle.load(open('chatbot_codes/words.pkl','rb'))
classes = pickle.load(open('chatbot_codes/classes.pkl','rb'))


from chatbot import routes
