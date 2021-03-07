from abc import ABC
import helper

import datetime
import random
import wikipedia
import webbrowser
import os
import pickle
import requests, json
import multiprocessing
import cv2
import time
import os.path
import pickle
import face_recognition
import virtual_assistant
import time as t
import virtual_assistant

from imutils import paths
from os import path
from covid import Covid

class Skill(ABC):
    """[summary]

    :param ABC: [description]
    :type ABC: [type]
    """
    def prepare(*argv):
        """[summary]
        """
        pass
    def run(*argv):
        """[summary]
        """
        pass
    def error(*argv):
        """[summary]
        """
        pass


class Covid19(Skill):
    """[summary]

    :param Skill: [description]
    :type Skill: [type]
    """
    def prepare(self, request:str, AIstatus:str, status:list):
        """[summary]

        :param request: [description]
        :type request: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        :return: [description]
        :rtype: [type]
        """
        AIstatus.value = status["process"]
        request = helper.remove_polite_words(request)
        city = helper.substring_after(request, "in")
        city = city.strip()
        print("[info city] ", city)
        return city

    def run(self, country, response, status, AIstatus):
        """[summary]

        :param country: [description]
        :type country: [type]
        :param response: [description]
        :type response: [type]
        :param status: [description]
        :type status: [type]
        :param AIstatus: [description]
        :type AIstatus: [type]
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
        response.value = answer["country"] + answer["newCases"] + answer["newDeaths"] + answer["activeCases"] + answer["recovered"] + answer["totalDeaths"]
        print(answer["answer"])
        AIstatus.value = status["answer"]
        virtual_assistant.speak(answer["answer"])

    def error(self, user:str, country:str, response:str, AIstatus:str, status:list):
        """[summary]

        :param user: [description]
        :type user: str
        :param country: [description]
        :type country: str
        :param response: [description]
        :type response: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        """
        answer = {"answer" : "Hmmm {}..., I cannot find any Covid19 statistics for {}.".format(user.value, country)}
        answer["help"] = "\n\n{} you can always ask me for help if you need.\nTry 'Pixel I need help!'".format(user.value)
        response.value = answer["answer"] + answer["help"]
        print(response.value)
        AIstatus.value = status["answer"]
        virtual_assistant.speak(answer["answer"])

class Thank_you(Skill):
    """[summary]

    :param Skill: [description]
    :type Skill: [type]
    """
    def prepare(self, user:str, AIstatus:str, status:list):
        """[summary]

        :param user: [description]
        :type user: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        :return: [description]
        :rtype: [type]
        """
        AIstatus.value = status["process"]
        thankYouAnswers = []
        thankYouAnswers.append("{} is always a pleasure to help you!".format(user.value))
        thankYouAnswers.append("{}, no problem, any time!".format(user.value))
        thankYouAnswers.append("{}, is always my pleasure!".format(user.value))
        thankYouAnswers.append("No problem {}, it was the least I could do.".format(user.value))
        thankYouAnswers.append("Glad to help you {}!".format(user.value))
        thankYouAnswers.append("Thank YOU, {}!".format(user.value))
        return random.choice(thankYouAnswers)

    def run(self, response:str, AIstatus:str, status:list, answer):
        """[summary]

        :param response: [description]
        :type response: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        :param answer: [description]
        :type answer: [type]
        """
        response.value = answer
        AIstatus.value = status["answer"]
        virtual_assistant.speak(response.value)


class Definition(Skill):
    """[summary]

    :param Skill: [description]
    :type Skill: [type]
    """
    def prepare(self, AIstatus:str, request:str, status:list):
        """[summary]

        :param AIstatus: [description]
        :type AIstatus: str
        :param request: [description]
        :type request: str
        :param status: [description]
        :type status: list
        :return: [description]
        :rtype: [type]
        """
        AIstatus.value = status["process"]
        request = helper.remove_polite_words(request)
        if "define" in request:
            word = helper.substring_after(request, "define")
        if "definition" in request:
            word = helper.substring_after(request, "definition")
        if "tell me about" in request:
            word = helper.substring_after(request, "tell me about")
        print("[INFO]", word)
        return word

    def run(self, response:str, AIstatus:str, word:str, status:list):
        """[summary]

        :param response: [description]
        :type response: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param word: [description]
        :type word: str
        :param status: [description]
        :type status: list
        """
        answer = []
        answer.append(wikipedia.summary(word, sentences=1, auto_suggest=False))
        answer.append(helper.niceFormattedLongText(answer[0]))
        print(answer[0])
        response.value = answer[1]
        AIstatus.value = status["answer"]
        virtual_assistant.speak(answer[0])

    def error(self, user:str, word:str, response:str, AIstatus:str, status:list):
        """[summary]

        :param user: [description]
        :type user: str
        :param word: [description]
        :type word: str
        :param response: [description]
        :type response: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        """
        answer = {"answer" : "Hmmm {}..., I am not sure I can provide a definition for {}.".format(user.value, word)}
        answer["help"] = "\n\n{} you can always ask me for help if you need.\nTry 'Pixel I need help!'".format(user.value)
        response.value = answer["answer"] + answer["help"]
        print(response.value)
        AIstatus.value = status["answer"]
        virtual_assistant.speak(answer["answer"])

class Help(Skill):
    """[summary]

    :param Skill: [description]
    :type Skill: [type]
    """
    def prepare(self, AIstatus:str, status:list, request:str):
        AIstatus.value = status["process"]
        if "with" in request:
            request = helper.remove_polite_words(request)
            help_for = helper.substring_after(request, "with")
            print("[info help_for] ", help_for)
        else:
            help_for = ""
        return help_for

    def run(self, subject:str, AIstatus:str, status:list, response:str, user:str):
        """[summary]

        :param subject: [description]
        :type subject: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        :param response: [description]
        :type response: str
        :param user: [description]
        :type user: str
        """
        help = ""
        if subject == "":
            help = "{}, I see you need some help! \nHere is how to interract with me:".format(user.value)
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
        response.value = help
        AIstatus.value = status["answer"]
        virtual_assistant.speak(response.value)

    def error(self, AIstatus:str, status:list, response:str, user:str):
        """[summary]

        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        :param response: [description]
        :type response: str
        :param user: [description]
        :type user: str
        """
        subject = ""
        self.run(subject, AIstatus, status, response, user)


class Location(Skill):
    """[summary]

    :param Skill: [description]
    :type Skill: [type]
    """
    def prepare(self, request:str):
        """[summary]

        :param request: [description]
        :type request: str
        :return: [description]
        :rtype: [type]
        """
        request = helper.remove_polite_words(request)
        request_words = ["open", "opening hour", "address", "where"]
        request = helper.remove_words(request, request_words)
        return request
    
    def run(self, AIstatus:str, location:str, response:str, status:list):
        """[summary]

        :param AIstatus: [description]
        :type AIstatus: str
        :param location: [description]
        :type location: str
        :param response: [description]
        :type response: str
        :param status: [description]
        :type status: list
        """
        with open('api_keys.json') as API:
            API = json.load(API)
            google_API = API['google']
        
        base_url_get_place_id = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=place_id&key={}".format(location, google_API)
        response_ID = helper.get_request(base_url_get_place_id)

        place_ID = str(response_ID['candidates'][0]['place_id'])
        base_url_get_location_details = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=opening_hours,name,rating,formatted_address,formatted_phone_number&key={}".format(place_ID, google_API)
        print(base_url_get_location_details)

        response_details = helper.get_request(base_url_get_location_details)
        isOpen = ""
        try:
            if response_details['result']['opening_hours']['open_now'] == True:
                isOpen = "Open at the moment. "
            else:
                isOpen = "Not open at the moment."
            location_details = {"answer" : "{} is {} {} phone number is {}".format(response_details['result']['name'], isOpen, response_details['result']['name'], response_details['result']['formatted_phone_number'])}
        except:
            location_details = {"answer" : "{} phone number is {}".format(response_details['result']['name'], response_details['result']['formatted_phone_number'])}
        location_details['name'] = "Name: " + response_details['result']['name'] + " is " 
        try:
            location_details['open_now'] = isOpen.lower() + "\n\n"
        except:
            location_details['open_now'] = ""
        location_details['address'] = helper.niceFormattedLongText("Address: " + response_details['result']['formatted_address'] + "\n\n")
        location_details['phone'] = "Phone number: " + response_details['result']['formatted_phone_number'] + "\n\n"
        
        try:
            opening_hours = str(response_details['result']['opening_hours']['weekday_text']).replace('\u2013', '-')
            opening_hours = opening_hours.replace(',','\n')
            opening_hours = opening_hours.replace("'", "\t")
            opening_hours = opening_hours.replace("[", "\n")
            opening_hours = opening_hours.replace("]", "")
            location_details['opening_hours'] = "Opening hours: " + opening_hours
        except:
            location_details['opening_hours'] = "Opening hours: " + "-"

        response.value = location_details["name"] + location_details["open_now"] + location_details["phone"] + location_details["address"] + location_details["opening_hours"]
        print(response.value)
        AIstatus.value = status["answer"]
        virtual_assistant.speak(location_details["answer"])

class Weather(Skill):
    """[summary]

    :param Skill: [description]
    :type Skill: [type]
    """
    def prepare(self, AIstatus:str, status:list, request:str):
        """[summary]

        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        :param request: [description]
        :type request: str
        :return: [description]
        :rtype: [type]
        """
        AIstatus.value = status["process"]
        city = helper.remove_polite_words(request)
        city = helper.substring_after(request, "in")
        city = helper.substring_after(request, "for")
        city = city.strip()
        return city

    def run(self, city:str, AIstatus:str, response:str, status:list):
        """[summary]

        :param city: [description]
        :type city: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param response: [description]
        :type response: str
        :param status: [description]
        :type status: list
        """
        with open('api_keys.json') as API:
            API = json.load(API)
            key = API['weather']
        base_url = "http://api.openweathermap.org/data/2.5/weather?q="
        complete_url = base_url + city + "&appid=" + key + "&units=metric"
        details = helper.get_request(complete_url)
        desc = str(details['weather'][0]['description'])
        temp = str(details['main']['temp'])
        #print(response)
        weather_details = {"answer" : "The weather in {} is\n {} and with the temperature of {} Celsius".format(city, desc, temp)}
        city = city.strip()
        city = city.capitalize()
        weather_details["location"] = "Location:\t" + city + "\n"
        weather_details["descrition"] = "Weather:\t" + desc + "\n"
        weather_details["temperature"] =  "Temperature: " + temp + "C \n"
        response.value = weather_details["location"]+ weather_details["descrition"]+ weather_details["temperature"]
        print(weather_details["answer"])
        AIstatus.value = status["answer"]
        virtual_assistant.speak(weather_details["answer"])

    def error(self, user:str, response:str, AIstatus:str, status:list, city:str):
        """[summary]

        :param user: [description]
        :type user: str
        :param response: [description]
        :type response: str
        :param AIstatus: [description]
        :type AIstatus: str
        :param status: [description]
        :type status: list
        :param city: [description]
        :type city: str
        """
        answer = {"answer" : "Hmmm {}..., I am not sure I can provide the forecast for {}.".format(user.value, city)}
        answer["help"] = "\n\n{} you can always ask me for help if you need.\nTry 'Pixel I need help!'".format(user.value)
        response.value = answer["answer"] + answer["help"]
        print(response.value)
        AIstatus.value = status["answer"]
        virtual_assistant.speak(answer["answer"])


class Good_bye(Skill):
    def prepare(self):
        byeAnswers = []
        byeAnswers.append("Good bye!")
        byeAnswers.append("See you soon")
        byeAnswers.append("Was a pleasure, see you soon")
        byeAnswers.append("See you later, aligator")
        byeAnswers.append("Bye bye")
        byeAnswers.append("Can't wait to meet again")
        return random.choice(byeAnswers)


    def run(self, AIstatus:str, response:str, message:str, status:list):
        AIstatus.value = status["process"]
        response.value = message
        AIstatus.value = status["answer"]
        virtual_assistant.speak(response.value)



