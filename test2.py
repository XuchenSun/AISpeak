from gtts import gTTS

import playsound

def speak(text):
    tts = gTTS(text=text, lang='en',tld='com.au')

    filename ="current.mp3"
    tts.save(filename)
    playsound.playsound(filename)


speak("Hi Xander. Sorry to bother you in vacation. We need your help.")