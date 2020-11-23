## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills
import display

questionAnswer = ''

def start(): 
    skills.speak(skills.greeting())
    while True:
        request = skills.inputVoiceCommand().lower()
        if "time" in request:
            answer = skills.time()
            skills.speak(answer)
            questionAnswer = answer

        if "date" in request:
            answer = skills.date()
            skills.speak(answer)
            questionAnswer = answer

        if "thank you" in request:
            answer = skills.responseThankYou()
            skills.speak(answer)
            questionAnswer = answer

        if "define" in request:
            answer = skills.wiki(request)
            skills.speak(answer)
            questionAnswer = answer

        if "definition" in request:
            answer = skills.wiki(request)
            skills.speak(answer)
            questionAnswer = answer

        if "see you" in request:
            answer = skills.responseBye()
            skills.speak(answer)
            questionAnswer = answer
            break

        if "bye" in request:
            answer = skills.responseBye()
            skills.speak(answer)
            questionAnswer = answer
            break


        