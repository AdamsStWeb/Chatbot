#Building a ChatBot with Deep NLP 


###### PreProcessing Data ###########

#Importing the libaries 

import numpy as np
import tensorflow as tp
import re
import time

#Import dataset

lines = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n') 
conversations = open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n') 

#map each line and their IDs 

id2line= {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]

# create a cleaned up list of the conversations 
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
    conversations_ids.append(_conversation.split(','))
        
#Get a list of questions and then a list of answers 
questions = []
answers = []
for conversation in conversations_ids:
    for i in range(len(conversation) -1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])



# First round of cleaning text 
def cleanText(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"you're", "you are", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~`|.?!,%$*]", "", text)
    return text
        


 
    
    
        
       


