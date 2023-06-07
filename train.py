#!/bin/python3
import random
import os
import pyttsx3
import time
#import vlc
#from gtts import gTTS


def produceAudio(number):
    engine = pyttsx3.init()
    engine.say(str(number))
    engine.runAndWait()
    #audioText = str(number)
    #language = "en"
    #obj = gTTS(text = audioText, lang=language, slow = False)
    #obj.save(fileName)
    #return fileName

for i in range(0, 10):
    number = random.randint(10, 99)
    produceAudio(number)
    #player = vlc.MediaPlayer(fileName)
    #player.play()
    inputing = input("please input:")
    if inputing == str(number):
        print("Great!!!")
    else:
        print("Sorry. it should be:" + str(number))
        time.sleep(3)
        
    
