## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills
import display
from multiprocessing import Process
import time

def startAI(response): 
    response.value = skills.greeting()
    skills.speak(response.value)
    while True:
        request = skills.inputVoiceCommand().lower()
        if "time" in request:
            response.value = skills.time()
            print(response.value)
            skills.speak(response.value)
            
        if "date" in request:
            response.value = skills.date()
            print(response.value)
            skills.speak(response.value)

        if "thank you" in request:
            response.value = skills.responseThankYou()
            print(response.value)
            skills.speak(response.value)

        if "define" in request:
            response.value = skills.wiki(request)
            skills.speak(response.value)

        if "definition" in request:
            response.value = skills.wiki(request)
            skills.speak(response.value)

        if "see you" in request:
            response.value = skills.responseBye()
            skills.speak(response.value)
            break

        if "bye" in request:
            response.value = skills.responseBye()
            skills.speak(response.value)
            break



        
        