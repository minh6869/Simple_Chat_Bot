import google.generativeai as palm
import translate

def AI(question):
    API_KEY = 'AIzaSyB2kNEdeRXNw9zIv2SVo1eoTomnwldusII'
    palm.configure(api_key=API_KEY)
    response = palm.chat(messages=question)
    s = response.last

    if s!= None:
       return s
    else:
        return "Hello! How can I help you today! "
# print(AI("hi"))

# resposne = response.reply("1+1=?")
# print(response.last)
