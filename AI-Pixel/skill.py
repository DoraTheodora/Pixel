from abc import ABC
import helper
import virtual_assistant

import random
import wikipedia

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