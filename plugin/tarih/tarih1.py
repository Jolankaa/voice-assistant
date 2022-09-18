import datetime
import locale
import playsound 
import os
from gtts import *

def speak(string):
    tts=gTTS(text=string, lang="tr")
    file="ansver.mp3"
    tts.save(file)
    playsound.playsound(file)
    os.remove(file)

def konus():
    locale.setlocale(locale.LC_ALL, '')
    an=datetime.datetime.now()
    ay=datetime.datetime.strftime(an, '%B')
    gün=datetime.datetime.strftime(an, '%A')
    saat=datetime.datetime.strftime(an, '%X')
    speak(f"{ay} ayındayız ve {gün} günündeyiz saatimiz ise {saat}")
