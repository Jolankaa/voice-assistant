# Title: Voice Assistant
# Date: 2022-08-10
# Author: jolanka
# Category: Helpful For life Software
# Version: 1.01
# Tested on : Windows 10 pro, Kali linux

#!/usr/bin/env python 3.10.5

#offical library
import os
from os import startfile
import time
import random
from requests import get

#translation func
def translate_to_msg(text_msg, to):
    
    a = get(f"https://translate.google.com/m?hl=auto&sl=auto&tl={to}&ie=UTF-8&prev=_m&q={text_msg}")
    html = a.text
    fin = html.split('result-container">')[1].split('</div>')[0]
    return fin



#required not offical library
try: 
    os.remove("ansver.mp3")
except:
    pass

#ERROR download colorama
try:
  from colorama import Fore, Back, Style, init
except ModuleNotFoundError:
    print("[+] Colorama Library is not loaded ❌")
    os.system("pip install colorama")
    print("[+] Problem Solved ✔️")
from colorama import Fore, Back, Style, init

#ERROR dowload playsound
try:
    from playsound import *
except ModuleNotFoundError:
    print(Fore.CYAN,"[+] Playsound Library is not loaded ❌ ")
    os.system("pip install playsound")
    print(Fore.CYAN,"[+] Problem Solved ✔️")
from playsound import *

#ERROR download gtts
try:
    from gtts import *
except ModuleNotFoundError:
    print(Fore.CYAN,"[+] gTTS Library is not loaded ❌ ")
    os.system("pip install gTTS")
    print(Fore.CYAN,"[+] Problem Solved ✔️")
from gtts import *

#ERROR download speech recogntition
try:
    import speech_recognition as sr
except ModuleNotFoundError:
    print(Fore.CYAN,"[+] SpeechRecognition Library is not loaded ❌ ")
    os.system("pip install SpeechRecognition")
    print(Fore.CYAN,"[+] Problem Solved ✔️")
import speech_recognition as sr

#file import //
from plugin.tarih.tarih1 import *
from poem import poem
from plugin.ezan.ezan import ezan
from plugin.karşılama.start import start
from plugin.developer_mode.developer import developer_mode
from ChatBot_src.main import chatbot
from key.app_key import main



liste=[
     "anlamadım lütfen düzgün söyle",
     "ya ben malım yada senin türkçen yok",
     "jolanka anlamadı yada anlamak istemedi",
     "düzgün konuş anlamıyorum",
     "rakiplerimden daha iyi anlama yeteneğine sahibim ama anlamadım"
    ]
#variable for unknw value error
unknownvalueError_x = random.choice(liste)

r=sr.Recognizer()
# ses algılama fonksiyonu
def record(ask = False):
    with sr.Microphone() as source:     #ses varsayılan mikrofondan alınır
        if ask:
            print(ask)
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio, language="tr-Tr")
        except sr.UnknownValueError:
            speak(unknownvalueError_x)
        except sr.RequestError:
            print(Fore.CYAN,"[+] Ağ Bağlantınızı Kontrol Ediniz .")
            os.startfile("RequestError.m4a")
            exit()
        except PlaysoundException:
            os.remove("ansver.mp3")
        return voice
        
def response(voice):
    command = (voice)
    if voice == "yazılımcı modu":
        developer_mode(command)
    if voice == "tarih" or voice=="bugün hangi gün"or voice=="hangi yıldayız" or "saat" in voice:
        konus()
    if voice == "hava durumu":
        a=os.popen('python hava_durumu.py').readline()
        speak(f"bugün{a}")
    if voice == "kapat" :
        exit()
    if voice=="oku" or voice=="şiir oku" or voice=="şiir okurmusun" :
        poem()
    if  voice=="ezan" or voice=="ezan vakitleri" :
        ezan()
    aftext =  translate_to_msg((voice), "en")
    chatbot(aftext)
    
def speak(string):
    tts=gTTS(text=string, lang="tr")
    file="ansver.mp3"
    tts.save(file)
    playsound.playsound(file)
    os.remove(file)                            #She can read all kinds of English words as her native language is English
                                               #O ingilizce ana dili olduğu için her türlü ingilzce konuşabilir
    
if main()==True:
    while True:
        
        voice=record()
        start()
        if voice !='':              #Whilenin içinde olmasının sebebi programın sürekli çalışması
            voice=voice.lower()
            print(voice)
            response(voice)


