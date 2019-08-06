#Building a ChatBot with Deep NLP 


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
    



