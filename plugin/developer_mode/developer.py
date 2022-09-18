import playsound,os
from gtts import *
import json
from requests import get
import datetime

def speak(string):
    tts=gTTS(text=string, lang="tr")
    file="ansver.mp3"
    tts.save(file)
    playsound.playsound(file)
    os.remove(file)                            #She can read all kinds of English words as her native language is English
                                               #O ingilizce ana dili olduğu için her türlü ingilzce konuşabilir
def developer_mode(command):
    an=datetime.datetime.now()
    saat=datetime.datetime.strftime(an, '%X')
    speak(f"{saat} Developer Modu Çalıştırılıyor tek yapmanız gereken çalıştırmanız gereken komutu söylemeniz")
    os.system(command)
