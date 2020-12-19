## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills
import display
from multiprocessing import Process
import time
from gtts import gTTS
import os
import speech_recognition as speech

def start(response, AIstatus): 
    response.value = skills.greeting()
    AIstatus.value = "Pixel is listening..."
    speak(response.value)

    while True:
        statusAndResquest = listen()
        request = statusAndResquest[2].lower()
        AIstatus.value = statusAndResquest[1]
        
        if "pixel" in request:
            if "time" in request:
                response.value = skills.time()
                print(response.value)
                speak(response.value)
                
            if "date" in request:
                response.value = skills.date()
                print(response.value)
                speak(response.value)
            
            if "weather" in request:
                response.value = skills.weather()
                print(response.value)
                speak(response.value)
            
            if "thank you" in request:
                response.value = skills.responseThankYou()
                print(response.value)
                speak(response.value)

            if "define" in request:
                response.value = skills.wiki(request)
                speak(response.value)

            if "definition" in request:
                response.value = skills.wiki(request)
                speak(response.value)

            if "see you" in request:
                response.value = skills.responseBye()
                speak(response.value)
                break

            if "bye" in request:
                response.value = skills.responseBye()
                speak(response.value)
                break




            
            AIstatus.value = statusAndResquest[0]

def listen():
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

def playAudiofile():
    os.system('cvlc text.mp3 --play-and-exit')

def speak(text):
    speakText = gTTS(text)
    speakText.save("text.mp3")
    playAudiofile()
    os.remove("text.mp3")
        
        