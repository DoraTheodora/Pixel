## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

## python text to speech 
import pyttsx3
import datetime
from gtts import gTTS
import os
import speech_recognition as speech
import random
import wikipedia

#engine = pyttsx3.init() 
#voices = engine.getProperty('voices')
#engine.setProperty('rate', 150) 
#engine.setProperty('voices', voices[0].id)

def playAudiofile():
    os.system('cvlc text.mp3 --play-and-exit')

def speak(text):
    #engine.say(text)
    #engine.runAndWait()
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
    speak(answer)

def responseThankYou():
    thankYouAnswers = []
    thankYouAnswers.append("Always a pleasure to help you")
    thankYouAnswers.append("No problem, any time")
    thankYouAnswers.append("My pleasure")
    thankYouAnswers.append("No problem, was the least I could do")
    thankYouAnswers.append("Glad to help")
    thankYouAnswers.append("Thank, YOU!")
    speak(random.choice(thankYouAnswers))    

def responseBye():
    byeAnswers = []
    byeAnswers.append("Good bye!")
    byeAnswers.append("See you soon")
    byeAnswers.append("Was a pleasure, see you soon")
    byeAnswers.append("See you later, aligator")
    byeAnswers.append("Bye bye")
    byeAnswers.append("Can't wait to meet again")
    speak(random.choice(byeAnswers))


def time():
    timeNow = "The time is "
    timeNow = timeNow +  datetime.datetime.now().strftime("%I:%M%p")
    speak(timeNow)

def date():
    dateNow = "Today's date is "
    dateNow = dateNow + datetime.datetime.now().strftime("%A%d%B%Y")
    speak(dateNow)

def greeting():
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour < 2:
        speak("Good night")
    elif hour < 12:
        speak("Good morning")
    elif hour < 17:
        speak("Good afternoon")
    elif hour < 22:
        speak("Good evening")
    else:
        speak("Good night")
    speak("How Pixel can assist you?")

def inputVoiceCommand():
    req = speech.Recognizer()
    with speech.Microphone() as microphoneSource:
        print("Pixel is listening...")
        req.pause_threshold = 1
        audio = req.listen(microphoneSource)
    try:
        print("Pixel heard you...")
        request = req.recognize_google(audio)
        print(request)
    except:
        print("Pixel cannot hear you...")
        speak("Say that again please")
        return "None"
    return request

