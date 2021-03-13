import speech_recognition as s
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import sched
import time
import os
import requests
import random
import wolframalpha
import pyautogui
import cv2
import winsound
import speedtest
d='how are you sir','whats your mood', 'what some thing refreshing tell me to play sonu nigam or ask some jokes', 'you can share with me anything','consider me as your best friend'
sr=s.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('i am jarvis')
engine.say(random.choice(d))
engine.runAndWait()
hour=datetime.datetime.now().hour
if hour>=6 and hour<=12:
     engine.say('Good morning')
     engine.runAndWait()
if hour>12 and hour<=18:
     engine.say('Good afternoon')
     engine.runAndWait()
if hour>=18 and hour<=24:
     engine.say('Good evening')
     engine.runAndWait()
if hour>=24:
     engine.say('Good night')
     engine.runAndWait()
engine.say('how can i help you sir')
engine.runAndWait()
def takeCommand():
    import speech_recognition as s

sr=s.Recognizer()
print("i am listening you ...............................")
app=wolframalpha.Client("JP2YWQ-77RG44KALT") 
with s.Microphone()as m:
    
     audio=sr.listen(m)
     query=sr.recognize_google(audio,language='eng-in')
     print(query)
     e='how can you compair foolish alexa with me','i didnt expect these from you sir','am i not able to fulfill your desire'
     k='never bunk your school sir ','have done your homework','i know you are a puntual guy'
if 'movie' in query:
          engine.say('opening movies sir')
          engine.runAndWait()
          webbrowser.open("https://myflixer.com")
if 'Google' in query:
          engine.say('opening google sir')
          engine.runAndWait()
          webbrowser.open("https://google.com")
if 'check weather' in query:
          engine.say('opening todays weather report sir')
          engine.runAndWait()
          webbrowser.open("https://www.accuweather.com")
if 'Amazon' in query:
          engine.say('sir in a mood of shopping immediately opening amazon')
          engine.runAndWait()
          webbrowser.open('https://www.amazon.in/')
if 'Flipkart' in query:
          engine.say('sir in a mood of shopping immediately opening flipkart')
          engine.runAndWait()
          webbrowser.open('https://flipkart.com')
if 'Gmail' in query:
          engine.say('opening gmail sir')
          engine.runAndWait()
          webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
if 'meet' in query:
          engine.say('want to get into meeting sir ok here it is')
          engine.runAndWait()
          webbrowser.open('https://meet.google.com')
if 'Vivo web share' in query:
          engine.say('opening vivo web share')
          engine.runAndWait()
          webbrowser.open('http://bs.vivo.com')
if 'Instagram' in query:
          engine.say('opening sir')
          engine.runAndWait()
          webbrowser.open('https://instagram.com')
if 'Reddit' in query:
          engine.say('opening sir')
          engine.runAndWait()
          webbrowser.open('https://www.reddit.com')
if 'Quora' in query:
          engine.say('opening sir')
          engine.runAndWait()
          webbrowser.open('https://www.quora.com')
if 'play'in query:
          video=query.replace('play', '')
          engine.say('playing'+ video)
          engine.runAndWait()
          pywhatkit.playonyt(query)
if 'time' in query:
          time=datetime.datetime.now().strftime('%H:%M:%S')
          engine.say("sir current time is"+ time)
          engine.runAndWait()
          print(time)
if 'who is' in query:
          person=query
          info=wikipedia.summary(person,1)
          engine.say(info)
          engine.runAndWait()
          print(info)
if 'friend' in query:
          engine.say('sure i am always for you sir')
          engine.runAndWait()
if 'are you single' in query:
          engine.say('ooooho i am in relation with Wifi')
          engine.runAndWait()
if 'jokes' in query:
          engine.say(pyjokes.get_joke())
          engine.runAndWait()
          print(pyjokes.get_joke())
if 'what is' in query:
          saman=query.replace('what is ', '')
          info=wikipedia.summary(saman,2)
          engine.say(info)
          engine.runAndWait()
          print(info)
if 'how are you' in query:
          engine.say('i am completely fine and full of energy')
          engine.runAndWait()
if 'do you eat' in query:
          engine.say('i eat WIFI and i excrete DATA')
          engine.runAndWait()
if 'birthday' in query:
          engine.say('HAPPY BIRTHDAY to you ')
          engine.runAndWait()
if 'you are a foolish' in query:
          engine.say('i am reflection of you is that enough to insult you ')
          engine.runAndWait()
if 'future' in query:
          engine.say('sir in two thousand ninty six i will make a time machine and gift to you then go to Albert eiensten and ask him')
          engine.runAndWait()
if 'ghost' in query:
          engine.say('there is only science in these world')
          engine.runAndWait()
if 'date' in query:
          now=datetime.datetime.now()
          l=now.strftime("%m%D%y")
          engine.say(l)
          engine.runAndWait()
          print(l)
if 'address' in query:
          engine.say('Meena ram residency shivmandir')
          engine.say('west bengal District Darjeeling city siliguri pincode 734011')
          engine.runAndWait()
if 'Alexa' in query:
          engine.say('sorry sir there is no sence of comparision i am better and smarter than them')
          engine.say(random.choice(e))
          engine.runAndWait()
if 'Maps' in query:
          engine.say('opening maps')
          engine.runAndWait()
          webbrowser.open('https://www.google.com/maps/@26.7157504,88.4015104,13z')
if 'Anubhab' in query:
          engine.say('sir Anubhab is my creator')
          engine.runAndWait()
if 'study Focus' in query:
          engine.say('sir i know its little hard but you can do it dont lose hope sir')
          engine.runAndWait()
          webbrowser.open('https://www.youtube.com/watch?v=RwxC5J8LI4Q')
if 'Chrome web store' in query:
          engine.say('opening chrome webstore sir')
          engine.runAndWait()
          webbrowser.open('https://chrome.google.com/webstore/category/extensions?utm_source=chrome-ntp-icon')
if 'classroom' in query:
          engine.say('go to your school sir')
          engine.say(random.choice(k))
          engine.runAndWait()
          webbrowser.open('https://classroom.google.com/u/1/h')
if 'exam' in query:
          engine.say('opening JEE MAINS MOCK TEST')
          engine.runAndWait()
          webbrowser.open('https://www.vedantu.com/test/PUBLIC/5dbd7cb0844b380beae8d15f')
if 'talk with me' in query:
          engine.say('why not sir')
          engine.runAndWait() 
          chatbot.main()
if "send whatapp message" in query:
          pywhatkit.sendwhatmsg("+91 98001 01028" "hi")
          time.sleep(5)
          engine.say('done')
          engine.runAndWait()
if 'where are we ' in query or 'where I am' in query:
          engine.say('wait sir searching')
          engine.runAndWait()
          res=requests.get('https://ipinfo.io/')
          data=res.json()
          city=data['city']

          location=data['loc'].split(',')
          latitude=location[0]
          longitude=location[1]  

          print("latitude: " , latitude)
          print("longitude: " , longitude)
          print("city: " , city)
          engine.say(city)
          engine.runAndWait()  
if 'are you ok' in query:
          engine.say('i am always ok baby what about you sir')
          engine.runAndWait()
          sr=s.Recognizer()
          print("i am listening you ...............................")
          with s.Microphone()as m:

              audio=sr.listen(m)
              query=sr.recognize_google(audio,language='eng-in')
              print(query) 
          if 'i am fine'in query:
               engine.say('thats i have never seen such coolest boss over the world')
               engine.runAndWait()
          else:
               engine.say('never be sad i am always there for you')
               engine.runAndWait()
if 'shut down' in query:
     engine.say('shutting the system go and get some rest sir')
     engine.runAndWait()
     os.system('shutdown /s /t 5')
if 'restart my system' in query:
     engine.say('restarting the system now i am lonely')
     engine.runAndWait()
     os.system('restart /r /t 5') 
if 'temperature' in query: 
     res=app.query(query)
     h=(next(res.results).text)
     engine.say("sir the current temperature is " +h)
     engine.runAndWait()         
     print(h)
if 'calculate' in query:
     engine.say('what should i calculate sir')
     engine.runAndWait()
     sr=s.Recognizer()
     print("i am listening you ...............................")
     with s.Microphone()as m:

          audio=sr.listen(m)
          query=sr.recognize_google(audio,language='eng-in')
          print(query)
          app=wolframalpha.Client("JP2YWQ-77RG44KALT")
          q=query 
          res=app.query(q)
          b=(next(res.results).text)
          engine.say(b)
          engine.runAndWait()
          print(b)
if 'open LinkedIn' in query:
     engine.say('sure opening sir')
     engine.runAndWait()
     webbrowser.open('https://www.linkedin.com/in/anubhab-chowdhury-517549204/')
if 'window' in query:
     pyautogui.keyDown("alt")
     pyautogui.press("tab")
     time.sleep(1)
     pyautogui.keyup("alt")
if 'news' in query:
     main_url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=61c35f9010d544859e1c1f63e51cbe67'
     main_page=requests.get(main_url).json()
     article=main_page["articles"]
     head=[]
     day=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
     for ar in article:
          head.append(ar["title"])
     for i in range(len(day)):
          engine.say(f"today's {day[i]} news is :{head[i]}")
          engine.runAndWait()
          print(f"today's {day[i]} news is :{head[i]}")
if 'camera'in query or 'Tamara' in query:
     engine.say('opening sir')
     engine.runAndWait()
     cam=cv2.VideoCapture(0)
     while cam.isOpened():
          ret, frame1=cam.read()
          ret, frame2=cam.read()
          diff=cv2.absdiff(frame1,frame2)
          gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
          blur=cv2.GaussianBlur(gray,(5,5), 0)
          _, thresh=cv2.threshold(blur,20,255, cv2.THRESH_BINARY)
          dilated=cv2.dilate(thresh,None,iterations=3)
          Contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
          #cv2.drawContours(frame1,Contours,-1,(0,255,0) , 2)
          for c in Contours:
               if cv2.contourArea(c) < 5000:
                    continue
               x,y,w,h=cv2.boundingRect(c)
               cv2.rectangle(frame1 , (x,y) , (x+w,y+h) ,(0,255,0) , 2)
               winsound.PlaySound('C:\\Users\\hp\Downloads\\Midnight-chimes-sound-effect\\.Midnight-chimes-sound-effects.MP3')
          if cv2.waitKey(10)==ord('q'):
               break
          cv2.imshow('smile', frame1)





     