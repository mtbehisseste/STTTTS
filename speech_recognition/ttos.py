# only avalible with python 2
import pyttsx3

engine = pyttsx3.init('neospeech')
engine.setProperty('rate', 135)

voices = engine.getProperty('voices')
# for voice in voices:
#     print (voice.id)
# print (voices[67].id)
engine.setProperty('voices', voices[67].id)

while True:
    try:
        x = input("Please input some words : ")
        engine.say(x)
        engine.runAndWait()

    except KeyboardInterrupt:
        break