Sheela
======
An Electronic Personal Assistant
---------------------------------------
- - -

Setup
------------------
####If you do not have the following, get them:
- Natural Language Toolkit http://www.nltk.org/

  1. sudo pip install -U nltk
  2. sudo pip install -U numpy
  3. In the Python Interpreter run

  - import nltk
  - nltk.download()
  
- Speech Recognition 3.1.3 https://pypi.python.org/pypi/SpeechRecognition/
  - pip install SpeechRecognition
- PortAudio
- PyAudio
  - pip install pyaudio
- flac

Google Speech API
--------------------
1. You will need to generate your own key at https://developers.google.com/api-client-library/python/guide/aaa_apikeys
2. After you have generated your key you will have to enable the Google Speech API
3. If this doesn't appear on the list of available API you will have to join the Chromium Dev List at https://groups.google.com/a/chromium.org/forum/#!forum/chromium-dev
