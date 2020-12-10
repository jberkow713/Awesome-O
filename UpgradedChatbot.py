import nltk
from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
import re  
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)
article = Article('https://www.rollingstone.com/music/music-features/eddie-van-halen-tribute-1081034/')
article.download()
article.parse()
article.nlp()
corpus = article.text

# print(corpus)

text = corpus
sentence_list = nltk.sent_tokenize(text)

#Got sentences in list from this specific article on Kidney issues
# print(sentence_list)



def greeting_response(text):

    text = text.lower()

    bot_greetings = ['Hello', 'hi', 'Hi there', "What's up fool?"]
    user_greetings = ['hi', 'hey', 'hello', 'howdy', 'hola']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

# print(greeting_response("hey there"))

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index        

def bot_response(user_input):

    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    #comparing last user_input to overall matrix
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    length_user_input = len(user_input)
    index = index[length_user_input:]
    response_flag = 0
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' ' + sentence_list[index[i]]
            response_flag = 1
            break
        
    if response_flag == 0:

        #didnt find similar sentence:
        # 
        bot_response = bot_response + ' ' + "Sorry, I could not find what you're looking for."     
    sentence_list.remove(user_input)
    return bot_response

def tokenize(article):

    #Take an article, based on a website, returns list of all words, Cleaned
    article.download()
    article.parse()
    article.nlp()
    corpus = article.text
    
    text = corpus
    sentence_list = nltk.sent_tokenize(text)

    Word_list = []
    
    Words2 = []
    Words = []
    
    for sentence in sentence_list:
        words = sentence.split()
        
        Word_list.append(words)
        
    stopwords = nltk.corpus.stopwords.words('english')

    for lists in Word_list:
        for word in lists:
            word = word.replace(",", "")
            word = word.replace(".", "")
            word = word.replace("?", "")
            word = word.lower()
            if '”' not in word and '“' not in word and '-' not in word and '/' not in word\
                and '(' not in word and ')' not in word:
            
                if word not in stopwords:
                    
                    Words2.append(word)
    
    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    for word in Words2:
        tokenizer.tokenize(word)
        if word not in Words:
            Words.append(word)


    return(Words)
    
def smarter_bot_response(user_input, article):

    user_input = user_input.lower()
    word_list = tokenize(article)
    # word_list gives us a list of words from the entire article
    # we want to compare each word in the user_input with words in the article to find highest correlated word
    # we want the bot to then create sentences piecing together words with highest correlation to highest correlated word

    #in order for this to work, we need to take the words in this list, and create sentences from them
    # in a way that first makes some sense, but also, puts correlated words together

    word_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(word_list)
    #comparing last user_input to overall matrix
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    #make sure it can not mimic the user's words
    length_user_input = len(user_input)


    
    index = index[2:]
    response_flag = 0
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' ' + word_list[index[i]]
            response_flag = 1
            break
        
    if response_flag == 0:

        #didnt find similar sentence:
        # 
        bot_response = bot_response + ' ' + "Sorry, I could not find what you're looking for."     
    word_list.remove(user_input)
    return bot_response    
    
    



# a = (tokenize(article))
# cm = CountVectorizer().fit_transform(a)
# print(cm)


print("I am Doc_Bot: I am here to help you learn about Eddie Van Halen")
print("What do you want to know?")
exit_list = ['exit', 'see you later', 'bye', 'quit']
while(True):
    user_input = input()
    if user_input in exit_list:
        print("See you later")
        break
    else:
        if greeting_response(user_input) != None:
            print("Doc Bot:" + greeting_response(user_input))
        else:
            print('Doc Bot:' + bot_response(user_input))    