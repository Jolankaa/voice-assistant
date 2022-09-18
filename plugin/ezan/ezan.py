# Title: Prayer Time
# Date: 2022-08-10
# Author: jolanka
# Category: Helpful For life Software
# Version: 1.01
# Tested on : Windows 10 pro 
# Special Thankx = Ber4tbey https://github.com/ber4tbey


import http.client
from tkinter import E 
import playsound,os
from gtts import *
import json

def ezan():
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "ezan.json",
        'authorization': "apikey 2dMupB4Lh50j0KxMhXToLm:1a1DbEQR6kh5FRFB5uvyOT"
    }
    conn.request("GET", "/pray/all?data.city=istanbul", headers=headers)
    res = conn.getresponse()
    data = res.read()
    a=data.decode("utf-8")
    object = json.loads(a)
    json_str = json.dumps(object, indent=2)
    e1 = object['result'][0]
    b=(e1['vakit'])
    c=(e1['saat'])
    e2 = object['result'][1]
    d=(e2['vakit'])
    e=(e2['saat'])
    e3 = object['result'][2]
    f=(e3['vakit'])
    g=(e3['saat'])
    e4 = object['result'][3]
    h=(e4['vakit'])
    ı=(e4['saat'])
    e5 = object['result'][4]
    i=(e5['vakit'])
    j=(e5['saat'])
    e6 = object['result'][5]
    k=(e6['vakit'])
    l=(e6['saat'])
    speak(f"namaz vakitleri {b},{c},{d},{e},{f},{g},{h},{ı},{i},{j},{k},{l}")

def speak(string):
    tts=gTTS(text=string, lang="tr")
    file="ansver.mp3"
    tts.save(file)
    playsound.playsound(file)
    os.remove(file)                         
