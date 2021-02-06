## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 December 2020

import requests

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
