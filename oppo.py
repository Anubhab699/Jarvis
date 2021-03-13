from gtts import gTTS
import os

fh=open("test.txt""r")
myText=fh.read().replace("\n","")

language='en'

output=gTTS(text=myText,lang=language,slow=False)

output.save("output.mp3");

os.system("Start output.mp3")
fh.close()
sr=s.Recognizer()
     print("i am listening you ...............................")
     app=wolframalpha.Client("JP2YWQ-77RG44KALT")
     sr.pause_threshold=1 
     with s.Microphone()as m:



     audio=sr.listen(m,timeout=4,phrase_time_limit=7)
     query=sr.recognize_google(audio,language='eng-in')
     print(query)
     def takeCommand():