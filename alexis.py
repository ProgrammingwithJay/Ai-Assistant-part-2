#import modules

import pyttsx3
import speech_recognition as sr
import time
import datetime
import webbrowser
import wikipedia


#initialization
print("Initializing Alexis")
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speakOut

def speakOut(text):
    engine.say(text)
    engine.runAndWait()

# speakOut("Programming with Jay")

#userInputs

def orders():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio=r.listen(source)
    try:
        print("recognizing")
        doubt=r.recognize_google(audio,language="en-Us")
        print("the user said: ",doubt)
    except Exception:
        speakOut("Sorry can you say it again")
        return "None"
    return doubt

#greet 

def greetUs():
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        print("good morning")
        speakOut(" good morning")
    elif 12<=hour<18:
        speakOut("Good afternoon")
    else:
        speakOut("Good evening")


greetUs()
speakOut("Hello I'm Alexis what I can do for you")
run=True
while run:
    doubt=orders().lower()
    if "wikipedia" in doubt:
        speakOut("Ok sir")
        doubt=doubt.replace("wikipedia","")
        result=wikipedia.summary(doubt, sentences=2)
        print(result)
        speakOut(result)
    elif "google" in doubt:
        webbrowser.open("https://www.google.com/")
    elif "stack overflow" in doubt:
        webbrowser.open("https://www.stackoverflow.com")
    elif "exit" in doubt:
        speakOut("Bye sir")
        run=False
        