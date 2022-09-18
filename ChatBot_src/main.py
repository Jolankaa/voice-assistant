# Title = ChatBot 
# Author = jolanka
# Version = 1.0.1alpha
# Special Thanks = https://github.com/ber4tbey

import playsound,os
from gtts import *
import json
from requests import get

def translate_to_msg(text_msg, to):
        a = get(f"https://translate.google.com/m?hl=auto&sl=auto&tl={to}&ie=UTF-8&prev=_m&q={text_msg}")
        

        html = a.text
        fin = html.split('result-container">')[1].split('</div>')[0]
        return fin
        
def chatbot(aftext):
    ass = get('http://api.brainshop.ai/get?bid=168815&key=9NeiB9TkAjUsKjkM&uid=' + "100" + f"&msg={aftext}").json()
    fin_msg = ass["cnt"]
                            
    outtext =  translate_to_msg(fin_msg, "tr")
    speak(outtext)
   

def speak(string):
    if os.path.isdir("ansver.mp3"):
        os.remove("ansver.mp3")
    tts=gTTS(text=string, lang="tr")
    file="ansver.mp3"
    tts.save(file)
    playsound.playsound(file)
                             
