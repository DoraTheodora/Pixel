## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills
import display
from multiprocessing import Process
import time

def startAI(response, AIstatus): 
    response.value = skills.greeting()
    AIstatus.value = "Pixel is listening..."
    skills.speak(response.value)

    while True:
        statusAndResquest = skills.inputVoiceCommand()
        request = statusAndResquest[2].lower()
        AIstatus.value = statusAndResquest[1]
        
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
        
        AIstatus.value = statusAndResquest[0]


        
        