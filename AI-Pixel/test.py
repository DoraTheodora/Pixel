import speech_recognition as speech

def record():
    re = speech.Recognizer()
    with speech.Microphone(device_index=3, sample_rate=48000) as source:
        print("Say something")
        re.pause_threshold = 1
        audio = re.listen(source, phrase_time_limit=3)
        print("Time stopped")
        try:
            request = re.recognize_google(audio, language='en')
            print(request)
        except:
            print("Did not work")


record()