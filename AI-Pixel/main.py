## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 21 November 2020

import skills

if __name__ == "__main__":
    skills.greeting()
    while True:
        request = skills.inputVoiceCommand().lower()
        if "time" in request:
            skills.time()
        if "date" in request:
            skills.date()
        if "thank you" in request:
            skills.responseThankYou()
        if "what is" in request:
            skills.wiki(request)
        if "define" in request:
            skills.wiki(request)
        if "definition" in request:
            skills.wiki(request)
        if "see you" in request:
            skills.responseBye()
            break
        if "bye" in request:
            skills.responseBye()
            break
        