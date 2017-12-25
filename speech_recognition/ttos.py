# only avalible with python 2
import pyttsx3

while True:
    try:
        engine = pyttsx3.init()
        print ("Please input some words:")
        x = input()
        engine.say(x)
        # engine.setProperty('rate',100) 
        engine.runAndWait()

    except KeyboardInterrupt:
        break