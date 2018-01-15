import pyttsx3

engine = pyttsx3.init('espeak')
engine.setProperty('rate', 160)

voices = engine.getProperty('voices')
engine.setProperty('voice', 'zh')

while True:
    try:
        x = input("Please input some words : ")
        engine.say(x)
        engine.runAndWait()

    except KeyboardInterrupt:
        break