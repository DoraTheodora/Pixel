## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 December 2020

def niceFormattedLongText(longString:str):
    """
        Method that formats a long string to multiple rows

        :param longString: is the string received from the virtual_assistant class, that needs to be formatatted
    """
    prettyString = ""
    for piece in splitter(5, longString):
        prettyString = prettyString + piece + "\n"
    return prettyString

def splitter(numberOfWords:int,longString:str):
    """
        Method created as a helper for the "niceFormattedLongText(longString:str)"  

        :param numberOfWords: denotes how many words are allowed on a single row
        :param longString: is the initial string that needs to be parsed
    """
    pieces = longString.split()
    answer = (" ".join(pieces[i:i+numberOfWords]) for i in range(0, len(pieces), numberOfWords))
    return answer

def substring_after(string:str, delimiter:str):
    """
        Method returning the next 2 words after a key word    

        :param string: is the initial string that needs to be parsed
        :param delimiter: is the key word searched in the string
    """
    answer = string.partition(delimiter)[2]
    answer.strip()
    return answer

def remove_polite_words(string:str):
    """
        Method removing the polite words from a string, as they are not used by the virtual_assistant to process a request

        :param string: initial string that neeeds polite words to be removed from it
    """
    string = string.replace("please", "")
    string = string.replace("thank you", "")
    string = string.replace("hello", "")
    return string
