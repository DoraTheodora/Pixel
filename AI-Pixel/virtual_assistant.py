## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills
import display
import helper
import skill

from gtts import gTTS
import os
import speech_recognition as speech

status = {
    "process" : "Pixel is processing...",
    "start" : "Pixel is starting...",
    "answer" : "Pixel has an answer...",}

def start(user:str, response:str, AIstatus:str, understanding:str, cameraRunning:bool): 
    """[This method starts the virtual assistant, that will processes the user's request and delivers a meaningful answer]

    :param user: [The user using the device]
    :type user: str
    :param response: [The text from the virtual's assistant response that is displayed to the screen]
    :type response: str
    :param AIstatus: [The virtual assistant's status that is displated to the screen]
    :type AIstatus: str
    :param understanding: [The user's voice input]
    :type understanding: str
    :param cameraRunning: [Main camera frame status]
    :type cameraRunning: bool
    """
    response.value = skills.greeting(user.value)
    AIstatus.value = status["start"]
    speak(response.value)

    while True:
        request = listening(AIstatus)
        request = request.lower()
        understanding.value = "Responding to: " + request
        
        if "pixel" in request:
            if "register" in request or "sign up" in request and not "help" in request:
                register = skill.Register()
                exists = register.user_exists(user, response)
                if exists == False:
                    name = register.get_name(AIstatus, response, understanding, user)
                    confirm = register.prepare(name)
                    if confirm == True:
                        register.run(AIstatus, cameraRunning, name, response, status)


            if "open" in request or "opening hour" in request or "address"  in request or "where" in request:
                location_details = skill.Location()
                request = location_details.prepare(request)
                location_details.run(AIstatus, request, response, status)

            if "help" in request:
                help = skill.Help()
                help_for = help.prepare(AIstatus, status, request)
                try:
                    help.run(help_for, AIstatus, status, response, user)
                except:
                    help.error(AIstatus, status, response, user)

            if "time" in request:
                time_now = skill.Time()
                now = time_now.prepare(AIstatus, status)
                time_now.run(now, AIstatus, response, status)
                
            if "date" in request:
                date_today = skill.Date()
                date = date_today.prepare(AIstatus, status)
                date_today.run(date, AIstatus, response, status)
            
            if "weather" in request and "help" not in request:
                #TODO: put forecast and temperature here
                weather = skill.Weather()
                city = weather.prepare(AIstatus, status, request)
                try:
                    weather.run(city, AIstatus, response, status)
                except:
                    weather.error(user, response, AIstatus, status, city) 

            if "covid" in request and "help" not in request:
                covid = skill.Covid19()
                country = covid.prepare(request, AIstatus, status)
                try:
                    covid.run(country, response, status, AIstatus)
                except:
                    covid.error(user, country, response, AIstatus, status)

            if "thank you" in request:
                thank_you_message = skill.Thank_you()
                answer = thank_you_message.prepare(user, AIstatus, status)
                thank_you_message.run(response, AIstatus, status, answer)

            if "define" in request or "definition" in request or "tell me about" in request:
                definition = skill.Definition()
                word = definition.prepare(AIstatus, request, status)
                try:
                    definition.run(response, AIstatus, word, status)
                except:
                    definition.error(user, word, response, AIstatus, status)

            if "bye" in request or "see you" in request:
                #TODO: verify if this works
                bye = skill.Good_bye()
                answer = bye.prepare()
                bye.run(AIstatus, response, answer, status)
        

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

def listen_for_name(AIStatus:str):
    req = speech.Recognizer()
    request = ""
    with speech.Microphone(device_index=3,sample_rate=48000) as microphoneSource:
        ## gathering the voice input
        AIStatus.value = "Pixel is listening..."
        req.adjust_for_ambient_noise(microphoneSource)
        req.pause_threshold = 0.5
        # TODO: ! phrase_time_limit needs to be removed!!!
        audio = req.listen(microphoneSource)#, phrase_time_limit=10)
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
        
        