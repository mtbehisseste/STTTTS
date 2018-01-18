from gtts import gTTS
import os

while True:
    try:
        inputStr = input("Type here: ")
        tts = gTTS(text = inputStr, lang = 'zh')
        tts.save("output.mp3")
        os.system("mpg123 -q output.mp3")

    except Exception:
        continue

    except KeyboardInterrupt:
        break
