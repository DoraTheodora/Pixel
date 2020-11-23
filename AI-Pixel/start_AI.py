## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills

def start(): 
    skills.speak(skills.greeting())
    while True:
        request = skills.inputVoiceCommand().lower()
        if "time" in request:
            skills.speak(skills.time())
        if "date" in request:
            skills.speak(skills.date())
        if "thank you" in request:
            skills.speak(skills.responseThankYou())
        if "what is" in request:
            skills.speak(skills.speak(skills.wiki(request)))
        if "define" in request:
            skills.speak(skills.wiki(request))
        if "definition" in request:
            skills.speak(skills.wiki(request))
        if "see you" in request:
            skills.speak(skills.responseBye())
            break
        if "bye" in request:
            skills.speak(skills.responseBye())
            break

if __name__ == "__main__":
    start()
        