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
    "answer" : "Pixel has an answer...",}

def start(user:str, response:str, AIstatus:str, understanding:str): 
    """[This method starts the virtual assistant, that will processes the user's request and delivers a meaningful answer]

    :param user: [The user using the device]
    :type user: str
    :param response: [The text from the virtual's assistant response that is displayed to the screen]
    :type response: str
    :param AIstatus: [The virtual assistant's status that is displated to the screen]
    :type AIstatus: str
    :param understanding: [The user's voice input]
    :type understanding: str
    """
    response.value = skills.greeting(user.value)
    AIstatus.value = status["start"]
    speak(response.value)

    while True:
        request = listening(AIstatus)
        request = request.lower()
        understanding.value = "Responding to: " + request
        
        if "pixel" in request:
            if "open" in request or "opening hour" in request or "address"  in request or "where" in request:
                try:
                    request = helper.remove_polite_words(request)
                    request_words = ["open", "opening hour", "address", "where"]
                    request = helper.remove_words(request, request_words)
                    answer = skills.location_details(request)
                    AIstatus.value = status["answer"]
                    print(answer)
                    response.value = answer["name"] + answer["open_now"] + answer["phone"] + answer["address"] + answer["opening_hours"]
                    speak(answer["answer"])
                except:
                    answer = skills.errorUnderstanding(user)
                    response.value = answer["answer"] + answer["help"]
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(answer["answer"])
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
                    answer = skills.errorUnderstanding(user)
                    response.value = answer["answer"] + answer["help"]
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(answer["answer"])

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
                    answer = skills.errorUnderstanding(user)
                    response.value = answer["answer"] + answer["help"]
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(answer["answer"])

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
                    answer = skills.errorUnderstanding(user)
                    response.value = answer["answer"] + answer["help"]
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(answer["answer"])

            if "thank you" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseThankYou()
                print(response.value)
                AIstatus.value = status["answer"]
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
                    answer = skills.errorUnderstanding(user)
                    response.value = answer["answer"] + answer["help"]
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(answer["answer"])

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
                    answer = skills.errorUnderstanding(user)
                    response.value = answer["answer"] + answer["help"]
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(answer["answer"])
            
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
                    answer = skills.errorUnderstanding(user)
                    response.value = answer["answer"] + answer["help"]
                    print(response.value)
                    AIstatus.value = status["answer"]
                    speak(answer["answer"])

            if "see you" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseBye()
                AIstatus.value = status["answer"]
                speak(response.value)

            if "bye" in request:
                AIstatus.value = status["process"]
                response.value = skills.responseBye()
                AIstatus.value = status["answer"]
                speak(response.value)


def listening(AIStatus:str):
    """[The method listens to the user's voice input (using voice recognition) and transforms it into text]

    :param AIStatus: [The virtual assistant's status: e.g.: processing, listeninging, etc]
    :type AIStatus: str
    :return: [The virtual assistant's response to the user's request]
    :rtype: [str]
    """
    req = speech.Recognizer()
    request = ""
    with speech.Microphone(device_index=3,sample_rate=48000) as microphoneSource:
        ## gathering the voice input
        AIStatus.value = "Pixel is listening..."
        req.pause_threshold = 0.5
        # TODO: ! phrase_time_limit needs to be removed!!!
        audio = req.listen(microphoneSource, phrase_time_limit=10)
        try:
            ## translate the voice input into text
            AIStatus.value = "Pixel heard you..."
            request = req.recognize_google(audio, language='en')
            print(request)
        except:
            ## if there was no voice input
            AIStatus.value = "Pixel cannot hear you..."
            speak("Say that again please")
            request = ""
            return request
    return request

def playAudiofile():
    """[Playing the virtual assistant's response back to the user by voice]
    """
    ## playing the audio file using vlc
    os.system('cvlc text.mp3 --play-and-exit')

def speak(text:str):
    """[This method transforms the virtual assistant's response from text to voice, using gTTS (Google's voice)]

    :param text: [String that needs to be transformed into an audio output]
    :type text: str
    """
    speakText = gTTS(text)
    ## saving the audio file
    speakText.save("text.mp3")
    ## playing the video file
    playAudiofile()
    ##removing the video file
    os.remove("text.mp3")
        
        