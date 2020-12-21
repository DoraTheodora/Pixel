## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 December 2020

def niceFormattedLongText(longString):
    prettyString = ""
    for piece in splitter(5, longString):
        prettyString = prettyString + piece + "\n"
    return prettyString

def splitter(n,s):
    pieces = s.split()
    answer = (" ".join(pieces[i:i+n]) for i in range(0, len(pieces), n))
    return answer

def substring_after(string, delimiter):
    answer = string.partition(delimiter)[2]
    return answer

def remove_polite_words(string):
    string = string.replace("please", "")
    string = string.replace("thank you", "")
    string = string.replace("hello", "")
    return string
