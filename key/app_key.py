from json import JSONDecodeError
from urllib import request
from requests import get
from gtts import * 
import os
from playsound import *


def speak(string):
    tts=gTTS(text=string, lang="tr")
    file="ansver.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)  

def main():
    start()
    user_key= input("key:")
    app_key = get('https://raw.githubusercontent.com/stragont/app_key/main/voice_assistant_key.json').json()
    final_msg= app_key["standart_key"]
    try:
        if user_key==final_msg:
            return True
    except JSONDecodeError:
        print("yanlışkey")        
    else:
        return False
    
def start():
    speak("sesli asistana hoşgeldiniz lütfen key giriniz")
    