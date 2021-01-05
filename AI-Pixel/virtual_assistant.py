## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills
import display
import helper


from multiprocessing import Process
import time
from gtts import gTTS
import os
import speech_recognition as speech

status = {
    "process" : "Pixel is processing...",
    "start" : "Pixel is starting...",
    "heard" : "Pixel heard you...",
    "listen" : "Pixel is listening...",
    "answer" : "Pixel has an answer...",
    "noSound" : "Pixel cannot hear you..."
}

def start(response, AIstatus): 
    """ This method starts the virtual assisstant, that will process the user's request
        and deliver a meaningful answer
        :param response.value: is the text from the virtual's assistant response that is displayed to the screen
        :param AIstatus.value: is the virtual assistant's status that is displated to the screen
        :param request: is the user's request in text format
    """

    response.value = skills.greeting()
    AIstatus.value = status["start"]
    speak(response.value)

    while True:
        AIstatus.value = status["listen"]
        statusAndResquest = listen()
        AIstatus.value = status["heard"]
        request = statusAndResquest[2].lower()
        
        if "pixel" in request:
            if "time" in request:
                AIstatus.value = status["process"]
                response.value = skills.time()
                AIstatus.value = status["answer"]
                print(response.value)
                speak(response.value)
                
            if "date" in request:
                AIstatus.value = status["process"]
                response.value = skills.date()
                AIstatus.value = status["answer"]
                print(response.value)
                speak(response.value)
            
            if "weather" in request:
                AIstatus.value = status["process"]
                try:
                    request = helper.remove_polite_words(request)
                    city = helper.substring_after(request, "in")
                    weatherDetails = skills.weather(city)
                    response.value = weatherDetails["location"]+ weatherDetails["descrition"]+ weatherDetails["temperature"]
                    AIstatus.value = status["answer"]
                    print(weatherDetails["answer"])
                    speak(weatherDetails["answer"])
                except:
                    response.value = skills.errorUnderstanding()
                    AIstatus.value = status["answer"]
                    print(response.value)
                    speak(response.value)

            if "thank you" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseThankYou()
                AIstatus.value = status["answer"]
                print(response.value)
                speak(response.value)

            if "define" in request:
                AIstatus.value = status["process"]
                request = helper.remove_polite_words(request)
                word = helper.substring_after(request, "define")
                try:
                    answer = skills.wiki(word)
                    response.value = answer[1]
                    AIstatus.value = status["answer"]
                    speak(answer[0])
                except:
                    response.value = skills.errorUnderstanding()
                    AIstatus.value = status["answer"]
                    print(response.value)
                    speak(response.value)

            if "definition" in request:
                AIstatus.value = status["process"]
                request = helper.remove_polite_words(request)
                word = helper.substring_after(request, "definition")
                try:
                    answer = skills.wiki(word)
                    response.value = answer[1]
                    AIstatus.value = status["answer"]
                    speak(answer[0])
                except:
                    response.value = skills.errorUnderstanding()
                    AIstatus.value = status["answer"]
                    print(response.value)
                    speak(response.value)
            
            if "tell me about" in request:
                AIstatus.value = status["process"]
                request = helper.remove_polite_words(request)
                word = helper.substring_after(request, "tell me about")
                try:
                    answer = skills.wiki(word)
                    response.value = answer[1]
                    AIstatus.value = status["answer"]
                    speak(answer[0])
                except:
                    response.value = skills.errorUnderstanding()
                    AIstatus.value = status["answer"]
                    print(response.value)
                    speak(response.value)

            if "see you" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseBye()
                AIstatus.value = status["answer"]
                speak(response.value)
                break

            if "bye" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseBye()
                AIstatus.value = status["answer"]
                speak(response.value)
                break


def listen():
    """The listen() function uses the speech_recognition to translate what the user's request is
    from voice to text
    """
    req = speech.Recognizer()
    status = ""
    actions = []
    with speech.Microphone() as microphoneSource:
        ## gathering the voice input
        status = "Pixel is listening..."
        actions.append(status)
        print(status)
        req.pause_threshold = 1
        audio = req.listen(microphoneSource)
    try:
        ## translate the voice input into text
        status = "Pixel heard you..."
        actions.append(status)
        print(status)
        request = req.recognize_google(audio)
        actions.append(request)
        print(request)
    except:
        ## if there was no voice input
        status = "Pixel cannot hear you..."
        actions.append(status)
        print(status)
        speak("Say that again please")
        actions.append("None")
        return actions
    for i in actions:
        print("-------", i)
        print(actions)
    return actions

def playAudiofile():
    ## playing the audio file using vlc
    os.system('cvlc text.mp3 --play-and-exit')

def speak(text):
    """ This function transforms the virtual asistant's response from test to speach"""
    speakText = gTTS(text)
    ## saving the audio file
    speakText.save("text.mp3")
    ## playing the video file
    playAudiofile()
    ##removing the video file
    os.remove("text.mp3")
        
        