from pprint import pprint
from urllib.request import urlopen
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re
from requests.api import request

def webscrapping():
    query = "weather sunday"
    words = query.split()
    words = get_synonyms(words)
    link = []
    for i in search(query, tld="com", num=2, stop=2, pause=2):
        link.append(i)
    webpage = requests.get(link[0]).text
    print (link[0])
    soup = BeautifulSoup(webpage, "lxml")
    paragraphs = soup.find('div')
    t = paragraphs.text
    all_text = t.splitlines()
    print(all_text)
    response = []
    for word in words:
        for phrase in all_text:
            if word in phrase:
                if phrase not in response:
                    response.append(phrase)
    for r in response:
        print(r, "\n")

def get_synonyms(words:list):
    ''' if "contact" or "phone" or "number" in words:
        words.append("tel")
        words.append("contact")
        words.append("phone")
        words.append("call")
    if "opening" or "hours" in words:
        words.append("monday")
        words.append("tuesday")
        words.append("wednesday")
        words.append("thursday")
        words.append("friday")
        words.append("sunday")
        words.append("saturday")
        words.append("tel")
        words.append("contact")
        words.append("phone")
        words.append("call") '''
    words = capitalize_words(words)
    print(words)
    return words

def capitalize_words(words:list):
    capitalize_list = []
    for word in words:
        capitalize_list.append(word.lower())
        capitalize_list.append(word.capitalize())
    return capitalize_list
        
webscrapping()