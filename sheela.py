import os
import speech_recognition as sr
import secrets
import handle

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print('What can I do for you?')
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    handle.request(r.recognize_google(audio, key=secrets.google_api_key))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
