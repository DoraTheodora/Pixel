## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 December 2020

import requests
import cv2
import os
import time
import os.path
import shutil
import virtual_assistant
import pickle

from os import path

def create_a_pickle_files(name:str):
    """[After registration this method creates two pickle files where the user's lists and settings will be stored]

    :param name: [name of the user and name of the folder where the pickle files are created]
    :type name: str
    """
    os.chdir("User/"+name)
    dictionaries = {}
    file_name = "user_lists"
    outfile = open(file_name, 'wb')
    pickle.dump(dictionaries, outfile)
    outfile.close()
    file_name = "user_settings"
    outfile = open(file_name, 'wb')
    pickle.dump(dictionaries, outfile)
    outfile.close()
    file_name = "SOS_contact"
    outfile = open(file_name, 'wb')
    pickle.dump(dictionaries, outfile)
    outfile.close()


def delete_pictures(name:str):
    """[Method that removes the pictures after registration, but keeps the folder for the user's personal settings and lists]

    :param name: [Name of the folder and name of the user]
    :type name: str
    """
    shutil.rmtree("User/"+name)
    os.mkdir("User/"+name)

def registration_diaglog(picture_number:int, name:str, len_images:int, response):
    """[Method that makes the registration interractive, by communicating with the user during the process]

    :param picture_number: [the number of picture that the process of training is at]
    :type picture_number: int
    :param name: [name of the user and name of the folder where the pictures are]
    :type name: str
    :param len_images: [the total number of pictures used for the registration process]
    :type len_images: int
    :param response: [response that is displayed on the screen to inform the user what the virtual assistant is saying]
    :type response: [type]
    """
    first_quarter = len_images//4
    second_quarter = first_quarter + first_quarter
    third_quarter = second_quarter + first_quarter
    if picture_number == first_quarter:
        response.value = "Looking good "  + name + "!\nI am starting to know you!"
        virtual_assistant.speak("Looking good " + name + " ! I am starting to know you!")
    elif picture_number == second_quarter:
        response.value = "You have very interesting features "  + name + "!\nWe are half way done."
        virtual_assistant.speak("You have very interesting features"  + name + "! We are half way done.")
    elif picture_number == third_quarter:
        response.value = name + " we are almost done! \nDo not go anywhere!"
        virtual_assistant.speak(name + " ! we are almost done! \nDo not go anywhere!")

def folder_exists(folder:str):
    """[The method checks is a certain path exists or not]

    :param folder: [The path that needs to be checked if it exists]
    :type folder: str
    :return: [returns True if the path exists, return False if the path does not exist]
    :rtype: str
    """
    if path.exists("User/"+folder):
        return True
    else:
        return False

def get_last_word(string:str):
    """[The method returns the last word from a sentence]

    :param string: [The sentence that needs to be parsed]
    :type string: str
    :return: [The last word of the sentence]
    :rtype: str
    """
    words = string.split(" ")
    last_word = words[-1]
    return last_word
    

def niceFormattedLongText(longString:str):
    """[Method that formats a long string to multiple rows]

    :param longString: [String received from the virtual_assistant class, that needs to be formatatted]
    :type longString: str
    """  
    prettyString = ""
    for piece in splitter(5, longString):
        prettyString = prettyString + piece + "\n"
    prettyString = prettyString + "\n"
    return prettyString

def splitter(numberOfWords:int,longString:str):
    """[Method created as a helper for the "niceFormattedLongText(longString:str)" ]

    :param numberOfWords: [Denotes how many words are allowed on a single row]
    :type numberOfWords: int
    :param longString: [The initial string that needs to be parsed]
    :type longString: str
    """
    pieces = longString.split()
    answer = (" ".join(pieces[i:i+numberOfWords]) for i in range(0, len(pieces), numberOfWords))
    return answer

def substring_after(string:str, delimiter:str):
    """[Method returning the next 2 words after a key word ]

    :param string: [Initial string]
    :type string: str
    :param delimiter: [The key word searched in the string]
    :type delimiter: str
    """
    answer = string.partition(delimiter)[2]
    return answer

def remove_words(string:str, words:list):
    """[summary]

    :param string: [String that neeeds to be cleaned]
    :type string: str
    :param words: [The words that the string needs to be cleaned from]
    :type words: list
    :return: [The cleaned string]
    :rtype: str
    """
    for word in words:
        string = string.replace(word, "")
    return string

def remove_polite_words(string:str):
    """[Method removing the polite words from a string, as they are not used by the virtual_assistant to process a request]

    :param string: [string that needs to cleaned from certain words]
    :type string: str
    """
    string = string.replace("please", "")
    string = string.replace("thank you", "")
    string = string.replace("hello", "")
    string = string.replace("the ", "")
    string = string.replace("for", "")
    string = string.replace("of", "")
    return string

def get_request(link:str):
    """[summary]

    :param link: [link to get the response from]
    :type link: str
    :return: [returns the response of the server in a json format]
    :rtype: [Json format]
    """
    response = requests.get(link) 
    response = response.json()
    return response
