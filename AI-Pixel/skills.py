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
import multiprocessing

from covid import Covid

def covidStatus(country:str):
    """[This skill provides the user, with covid-19 statistics from www.worldometers.info]

    :param country: [the country that the user requests info]
    :type country: str
    :return: [a dictionary with all the information regarding the contry in question]

        ["country"] = country

        ["newCases"] = new cases reported in the country

        ["newDeaths"] = new deaths reported in the country

        ["activeCases"] = current active cases in the country

        ["recovered"] = total number of cases recovered in the country

        ["totalDeaths"] = total number of deaths from Covid-19 in the country

    :rtype: dictionary
    """
    covid19 = Covid(source="worldometers")
    covidResults = covid19.get_status_by_country_name(country)
    country = covidResults["country"]
    activeCases = covidResults["active"]
    totalDeaths = covidResults["deaths"]
    newDeaths = covidResults["new_deaths"]
    newCases = covidResults["new_cases"]
    recovered = covidResults["recovered"]
    answer = {"answer" : "In {} there are {} new cases and {} new deaths".format(country, newCases, newDeaths)}
    answer["country"] = "Country: " + country + "\n"
    answer["newCases"] = "New Cases: " + str(newCases) + "\n"
    answer["newDeaths"] = "New deaths: " + str(newDeaths) + "\n"
    answer["activeCases"] = "Total active cases: " + str(activeCases) + "\n"
    answer["recovered"] = "Total recovered cases: " + str(recovered) + "\n"
    answer["totalDeaths"] = "Total deaths: " + str(totalDeaths) + "\n"
    return answer

def help(subject:str, user:str):
    """[summary]

    :param subject: [description]
    :type subject: str
    :param user: [description]
    :type user: str
    :return: [description]
    :rtype: [type]
    """
    help = ""
    if subject == "":
        help = "{}, I see you need some help! \nHere is how to interract with me:".format(user)
        help = help + "\n\n   1. Pixel what is the time/date"
        help = help + "\n   2. Pixel covid-19 stats in Ireland"
        help = help + "\n   3. To define a word: \n \t - Pixel tell me about dinosaurs \n \t - Pixel define dinosaur"
        help = help + "\n   4. Pixel tell me the weather in Dublin"
        help = help + "\n   5. To stop the conversation, step away from the mirror"
        help = help + "\n\n! Remember that every command needs to start with PIXEL !"
    if "weather" in subject:
        help = "{}, I see you need some help! \nHere is how to ask for weather forecast:".format(user.value)
        help = help + "\n\n    1. Pixel tell me the weather in Dublin"
        help = help + "\n    2. Pixel how is the weather in Dublin?"
        help = help + "\n    3. Pixel weather in Dublin"
        help = help + "\n    4. Keep in mind you can use any city"
        help = help + "\n\n! Remember that every command needs to start with PIXEL !"
    if "covid" in subject:
        help = "{}, I see you need some help! \nHere is how to ask for Covid-19 statistics:".format(user.value)
        help = help + "\n\n    1. Pixel tell me covid stats in Ireland"
        help = help + "\n    2. Pixel how is covid situation in Ireland?"
        help = help + "\n    3. Pixel how is the covid situation in Ireland?"
        help = help + "\n    4. Keep in mind you can use any country"
        help = help + "\n\n! Remember that every command needs to start with PIXEL !"
    return help

def errorUnderstanding(user):
    
    """ [summary] If the virtual assistant is not able to handle the request """
    answer = "Sorry I did not get that, please try again!"
    answer = answer + "\n\n{} you can always ask me for help if you need".format(user.value)
    answer = answer + "\nTry 'Pixel I need help'"
    return answer

def weather(city:str):
    """[summary]

    :param city: [description]
    :type city: str
    :return: [description]
    :rtype: [type]
    """
    with open('api_keys.json') as API:
        API = json.load(API)
        key = API['weather']
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    complete_url = base_url + city + "&appid=" + key + "&units=metric"
    response = requests.get(complete_url)
    response = response.json()
    desc = str(response['weather'][0]['description'])
    temp = str(response['main']['temp'])
    #print(response)
    answer = {"answer" : "The weather in {} is\n {} and with the temperature of {} Celsius".format(city, desc, temp)}
    city = city.strip()
    city = city.capitalize()
    answer["location"] = "Location:\t" + city + "\n"
    answer["descrition"] = "Weather:\t" + desc + "\n"
    answer["temperature"] =  "Temperature: " + temp + "C \n"
    print(answer)
    return answer


def restartDevice():
    os.system("shutdown -l")
    ## more work here, to make the device restart


def wiki(request:str):
    """[summary]

    :param request: [description]
    :type request: str
    :return: [description]
    :rtype: [type]
    """
    request = request.replace("pixel", "")
    request = request.replace("wikipedia", "")
    request = request.replace("what is", "")
    request = request.replace("define", "")
    request = request.replace("definition", "")
    answer = []
    answer.append(wikipedia.summary(request, sentences=1))
    answer.append(helper.niceFormattedLongText(answer[0]))
    print(answer[0])
    return answer

def responseThankYou():
    """[summary]

    :return: [description]
    :rtype: [type]
    """
    thankYouAnswers = []
    thankYouAnswers.append("Always a pleasure to help you")
    thankYouAnswers.append("No problem, any time")
    thankYouAnswers.append("My pleasure")
    thankYouAnswers.append("No problem, was the least I could do")
    thankYouAnswers.append("Glad to help")
    thankYouAnswers.append("Thank, YOU!")
    return random.choice(thankYouAnswers)

def responseBye():
    """[summary]

    :return: [description]
    :rtype: [type]
    """
    byeAnswers = []
    byeAnswers.append("Good bye!")
    byeAnswers.append("See you soon")
    byeAnswers.append("Was a pleasure, see you soon")
    byeAnswers.append("See you later, aligator")
    byeAnswers.append("Bye bye")
    byeAnswers.append("Can't wait to meet again")
    return random.choice(byeAnswers)

def time():
    """[summary]

    :return: [description]
    :rtype: [type]
    """
    timeNow = "The time is "
    timeNow = timeNow +  datetime.datetime.now().strftime("%I:%M %p")
    return timeNow

def date():
    """[summary]

    :return: [description]
    :rtype: [type]
    """
    dateNow = "Today's date is "
    dateNow = dateNow + datetime.datetime.now().strftime("%A %d %B %Y")
    return dateNow

def greeting(user):
    """[summary]

    :param user: [description]
    :type user: [type]
    :return: [description]
    :rtype: [type]
    """
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
    timeOfDay = timeOfDay + " " + user +  "! How Pixel can assist you?"
    return timeOfDay




