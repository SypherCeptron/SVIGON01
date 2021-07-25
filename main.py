import cv2
import pyttsx3
from time import time
from BFT import BFT
from ColorReco import ColorReco
from SpeechReco import SpeechReco,SilentSpeechReco
import datetime

def Redirector(x):
    #Gets the best fram
    frame = BFT()
    #module selections
    if(x == 1): Aud = ColorReco(frame)

    #coverting text into voice
    engine = pyttsx3.init()
    engine.say(Aud)
    engine.runAndWait()
    ActiveListener()



def ActiveListener():
    start = time()

    while (1):
        #listning to User's to user cammands
        Transcription = SpeechReco()
        if Transcription == "time":
            engine = pyttsx3.init()
            #getting todays date and time
            x = datetime.datetime.now()
            DateTime = x.strftime("Today's date is %A %d %B %Y and time is %H %M %S")
            engine.say(DateTime)
            engine.runAndWait()
            ActiveListener()
            break
        if Transcription == "colour":
            Redirector(1)
            break
        #incase of invalid commands
        if Transcription != "time" or Transcription != "color" or Transcription != "sleep":
            engine = pyttsx3.init()
            engine.say("Can you please repeat")
            engine.runAndWait()
        #putting back to silentlistner manually
        if Transcription == "sleep":
            engine = pyttsx3.init()
            engine.say("I am going back to sleep")
            engine.runAndWait()
            Silentlistener()
        stop = time()
        #incase the user leaves the device on
        if int(stop-start) > 10:
            engine = pyttsx3.init()
            engine.say("I am going back to sleep")
            engine.runAndWait()
            Silentlistener()
#Voice activation/keyword

def Silentlistener():
    SilentSpeechReco()
    engine = pyttsx3.init()
    engine.say("Ask me something")
    engine.runAndWait()
    ActiveListener()
#Main initializer
Silentlistener()


