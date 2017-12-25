import speech_recognition as sr

r = sr.Recognizer()
while True:
    try:
        with sr.Microphone(sample_rate=16000) as source:
            print("Speak:")
            audio = r.listen(source)
        try:
            print(r.recognize_google(audio, language="zh-TW"))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

    except KeyboardInterrupt:
        break