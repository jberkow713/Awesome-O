# To create virtual environment python -m venv "name_of_environment"-env
# Go to place where you want to activate it and then do below steps
# To enter virtual environment : Chatbot-env\Scripts\activate
# To exit virtual environment : deactivate


import nltk
from nltk.chat.util import Chat, reflections

# print(Chat)
# print(reflections)

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name?",
        ["You can call me a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you? ",
        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can check their website",]
    ],
    [r"How is the weather?",
    ["Why don't you check the weather reports you lazy asshole??!"]],
    
    
    [
        r"thanks for the suggestion. do they have great authors and instructors?",
        ["Yes, they have the world class best authors, that is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]


print(reflections)
chat = Chat(set_pairs, reflections)
# print(chat)

def chatbot():
        print("Hi, I'm the chatbot you built") 

chatbot()

chat.converse()
if __name__ == "__main__":
    chatbot()