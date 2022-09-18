import playsound
from gtts import *
import os
import random

try:
    from colorama import Fore
except ModuleNotFoundError:
    print("[!] Kütüphane bulunamadı hatası, çözülüyor")
    os.system("pip install colorama")
    print("kütüphane sorunu çözüldü")

def speak(string):
    tts=gTTS(text=string, lang="tr")
    file="ansver.mp3"
    tts.save(file)
    playsound.playsound(file)
    os.remove(file)


def start():
    start_dic=["dinliyorum",
            "program açık",
            "seni dinliyorum"
            ]
    start = random.choice(start_dic)
    
    
    öneriler_dic = ["saat kaç",
                    "ezan vakitleri",
                    "naber",
                    "develeper mode"]
    öneriler = random.choice(öneriler_dic)

    print(Fore.GREEN,
                    f"{öneriler}")
    speak(start)