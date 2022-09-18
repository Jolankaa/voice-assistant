from logging.config import listen
import os
import random
from gtts import *
import playsound


def speak(string):
    tts=gTTS(text=string, lang="tr")
    file="ansver.mp3"
    tts.save(file)
    playsound.playsound(file)
    os.remove(file)                      

def poem():
    liste=[
    "Açardın,YalnızlığımdaMavi ve yeşil,Açardın.Tavşan kanı, kınalı - berrak.Yenerdim acıları, kahpelikleri...",
    "Sana bir uygarlığı getirdim; anlamadın Yavuz kahramanları, şiirin burçlarını Ayak ucuna koydum gecenin saçlarını Urganmış boynumda taşıdığın gerdanlık Sana hükümdarlığı getirdim; anlamadın",
    "Seni bir yıldız gibi koyacağım göklere Her gece ışığını ruhumdan alacaksın Aldanma gururunu okşayan çiçeklere En güzel güllerini ruhumla alacaksın",
    "Artık demir almak günü gelmişse zamandan,Meçhule giden bir gemi kalkar bu limandan.Hiç yolcusu yokmuş gibi sessizce alır yol; Sallanmaz o kalkışta ne mendil ne de bir kol."
    "Aşk savaşmaktır.Aşk gülümsemektir.Aşk kırgınlığı yok sayıp,mutluluğu yaşamaktır.Ben seninle yaşanılan her mutluluğu ölümsüz bir anı olarak gönül haneme kaydettim sevdiğim"
    ]
    r_poem = random.choice(liste)
    speak(r_poem)
