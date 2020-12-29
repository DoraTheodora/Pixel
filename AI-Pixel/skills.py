## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020
import helper


import datetime
import random
import wikipedia
import webbrowser
import os
import pickle
import requests, json

def errorUnderstanding():
    """ If the virtual assistant is not able to handle the request """
    answer = "Sorry I did not get that, please try again!"
    return answer

def weather(city:str):
    with open('api_keys.json') as API:
        API = json.load(API)
        key = API['weather']
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    city = city.capitalize()
    complete_url = base_url + city + "&appid=" + key + "&units=metric"
    response = requests.get(complete_url)
    response = response.json()
    desc = str(response['weather'][0]['description'])
    temp = str(response['main']['temp'])
    #print(response)
    answer = {"answer" : "The weather in {} is\n {} and with the temperature of {} Celsius".format(city, desc, temp)}
    answer["location"] = "Location: " + city + "\n"
    answer["descrition"] = "Weather: " + desc + "\n"
    answer["temperature"] =  "Temperature: " + temp + "C \n"
    print(answer)
    return answer


def restartDevice():
    os.system("shutdown -l")
    ## more work here, to make the device restart


def wiki(request:str):
    request = request.replace("pixel", "")
    request = request.replace("wikipedia", "")
    request = request.replace("what is", "")
    request = request.replace("define", "")
    request = request.replace("definition", "")
    answer = []
    answer.append(wikipedia.summary(request, sentences=2))
    answer.append(helper.niceFormattedLongText(answer[0]))
    print(answer[0])
    return answer

def responseThankYou():
    thankYouAnswers = []
    thankYouAnswers.append("Always a pleasure to help you")
    thankYouAnswers.append("No problem, any time")
    thankYouAnswers.append("My pleasure")
    thankYouAnswers.append("No problem, was the least I could do")
    thankYouAnswers.append("Glad to help")
    thankYouAnswers.append("Thank, YOU!")
    return random.choice(thankYouAnswers)

def responseBye():
    byeAnswers = []
    byeAnswers.append("Good bye!")
    byeAnswers.append("See you soon")
    byeAnswers.append("Was a pleasure, see you soon")
    byeAnswers.append("See you later, aligator")
    byeAnswers.append("Bye bye")
    byeAnswers.append("Can't wait to meet again")
    return random.choice(byeAnswers)

def time():
    timeNow = "The time is "
    timeNow = timeNow +  datetime.datetime.now().strftime("%I:%M %p")
    return timeNow

def date():
    dateNow = "Today's date is "
    dateNow = dateNow + datetime.datetime.now().strftime("%A %d %B %Y")
    return dateNow

def greeting():
    hour = int(datetime.datetime.now().strftime("%H"))
    timeOfDay = ""
    if hour < 2:
        timeOfDay = timeOfDay + "Good night"
    elif hour < 12:
        timeOfDay = timeOfDay + "Good morning"
    elif hour < 17:
        timeOfDay = timeOfDay + "Good afternoon"
    elif hour < 22:
        timeOfDay = timeOfDay + "Good evening"
    else:
        timeOfDay = timeOfDay + "Good night"
    timeOfDay = timeOfDay + ". How Pixel can assist you?"
    return timeOfDay



