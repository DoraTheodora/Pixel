## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

## python text to speech 
import datetime
from gtts import gTTS
import os
import speech_recognition as speech
import random
import wikipedia

def playAudiofile():
    os.system('cvlc text.mp3 --play-and-exit')

def speak(text):
    speakText = gTTS(text)
    speakText.save("text.mp3")
    playAudiofile()
    os.remove("text.mp3")

def wiki(request):
    request = request.replace("wikipedia", "")
    request = request.replace("what is", "")
    request = request.replace("define", "")
    request = request.replace("definition", "")
    answer = wikipedia.summary(request, sentences=2)
    print(answer)
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

def inputVoiceCommand():
    req = speech.Recognizer()
    status = ""
    actions = []
    with speech.Microphone() as microphoneSource:
        status = "Pixel is listening..."
        actions.append(status)
        print(status)
        req.pause_threshold = 1
        audio = req.listen(microphoneSource)
    try:
        status = "Pixel heard you..."
        actions.append(status)
        print(status)
        request = req.recognize_google(audio)
        actions.append(request)
        print(request)
    except:
        status = "Pixel cannot hear you..."
        actions.append(status)
        print(status)
        speak("Say that again please")
        actions.append("None")
        return actions
    for i in actions:
        print("-------", i)
    return actions

