import os
import sys
import speech_recognition as sr
import secrets
import format

import webbrowser

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`

    # Prints result of voice
    # print("Google Speech Recognition thinks you said " + r.recognize_google(audio, key=secrets.google_api_key))

    # Says it right back to you
    # os.system("say " + format.for_say(r.recognize_google(audio, key=secrets.google_api_key)))

    # Google Searches it
    url = "https://www.google.com/#q=" + format.for_google_search(r.recognize_google(audio, key=secrets.google_api_key))
    webbrowser.open(url, new=2)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
