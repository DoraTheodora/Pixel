## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills
import display
import helper


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

def start(user:str, response:str, AIstatus:str, understanding:str): 
    """ 
        This method starts the virtual assistant, that will process the user's request and deliver a meaningful answer

        :param response: is the text from the virtual's assistant response that is displayed to the screen
        :param AIstatus: is the virtual assistant's status that is displated to the screen
        :param request: is the user's request in text format
    """

    response.value = skills.greeting(user.value)
    AIstatus.value = status["start"]
    speak(response.value)

    while True:
        request = listen(AIstatus)
        request = request.lower()
        understanding.value = "Responding to: " + request
        
        if "pixel" in request:
            if "help" in request:
                try:
                    AIstatus.value = status["process"]
                    if "with" in request:
                        request = helper.remove_polite_words(request)
                        help_for = helper.substring_after(request, "with")
                        print("[info help_for] ", help_for)
                        response.value = skills.help(help_for, user)
                    else:
                        response.value = skills.help("", user.value)
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(response.value)
                except:
                    response.value = skills.errorUnderstanding(user)
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(response.value)

            if "time" in request:
                AIstatus.value = status["process"]
                response.value = skills.time()
                print(response.value)
                speak(response.value)
                
            if "date" in request:
                AIstatus.value = status["process"]
                response.value = skills.date()
                print(response.value)
                speak(response.value)
            
            if "weather" in request and "help" not in request:
                AIstatus.value = status["process"]
                try:
                    request = helper.remove_polite_words(request)
                    city = helper.substring_after(request, "in")
                    weatherDetails = skills.weather(city)
                    response.value = weatherDetails["location"]+ weatherDetails["descrition"]+ weatherDetails["temperature"]
                    print(weatherDetails["answer"])
                    AIstatus.value = status["answer"]
                    speak(weatherDetails["answer"])
                except:
                    response.value = skills.errorUnderstanding(user)
                    print(response.value)
                    speak(response.value)

            if "covid" in request and "help" not in request:
                AIstatus.value = status["process"]
                try:
                    request = helper.remove_polite_words(request)
                    city = helper.substring_after(request, "in")
                    city = city.strip()
                    print("[info city] ", city)
                    covidStats = skills.covidStatus(city)
                    response.value = covidStats["country"] + covidStats["newCases"] + covidStats["newDeaths"] + covidStats["activeCases"] + covidStats["recovered"] + covidStats["totalDeaths"]
                    print(covidStats["answer"])
                    AIstatus.value = status["answer"]
                    speak(covidStats["answer"])
                except:
                    response.value = skills.errorUnderstanding(user)
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(response.value)

            if "thank you" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseThankYou()
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
                    response.value = skills.errorUnderstanding(user)
                    print(response.value)
                    AIstatus.value = status["answer"]
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
                    response.value = skills.errorUnderstanding(user)
                    print(response.value)
                    AIstatus.value = status["answer"]
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
                    response.value = skills.errorUnderstanding(user)
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(response.value)

            if "see you" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseBye()
                speak(response.value)

            if "bye" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseBye()
                speak(response.value)


def listen(AIStatus:str):
    """The listen() function uses the speech_recognition to translate what the user's request 
    from voice to text
    """
    req = speech.Recognizer()
    request =""
    with speech.Microphone() as microphoneSource:
        ## gathering the voice input
        AIStatus.value = "Pixel is listening..."
        req.pause_threshold = 1
        audio = req.listen(microphoneSource)
    try:
        ## translate the voice input into text
        AIStatus.value = "Pixel heard you..."
        request = req.recognize_google(audio)
        print(request)
    except:
        ## if there was no voice input
        AIStatus.value = "Pixel cannot hear you..."
        speak("Say that again please")
        request = "None"
        return request
    #for i in actions:
        #print("-------", i)
        #print(actions)
    return request

def playAudiofile():
    ## playing the audio file using vlc
    os.system('cvlc text.mp3 --play-and-exit')

def speak(text:str):
    """ This function transforms the virtual asistant's response from test to speach"""
    speakText = gTTS(text)
    ## saving the audio file
    speakText.save("text.mp3")
    ## playing the video file
    playAudiofile()
    ##removing the video file
    os.remove("text.mp3")
        
        