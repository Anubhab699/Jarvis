from gtts import gTTS
import os

fh=open("test.txt""r")
myText=fh.read().replace("\n","")

language='en'

output=gTTS(text=myText,lang=language,slow=False)

output.save("output.mp3");

os.system("Start output.mp3")
fh.close()
