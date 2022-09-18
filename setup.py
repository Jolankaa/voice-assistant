# Title = jolanka voice assistant setup file
# Author = jolanka
# Version = 1.2.0alpha
# Tested on = Windows 10 pro, Kali linux

#import Offical Library 
import time
import sys
import os
from platform import system
import datetime
#Function Written To Download Libraries
an=datetime.datetime.now()
saat=datetime.datetime.strftime(an, '%X')

def package():
    ani()
    if system()=="Linux":
        os.system("clear")
    if system()=="Windows":
        os.system("cls")
    if system() == "Linux":
        try:
            #download SpeechRecognition library for linux
            os.system("pip install SpeechRecognition")
            print(f"[{saat}][+] Speech Recognition Kütüphanesi Yüklendi ✔️")
            #download gtts library for linux
            os.system("pip install gtts")
            print(f"[{saat}][+] GTTS Kütüphanesi Yüklendi ✔️")
            #download playsound library for linux
            os.system("pip install playsound")
            print(f"[{saat}][+] Playsound Kütüphanesi Yüklendi ✔️")
            #download  requests library for linux
            os.system("pip3 install requests")
            print(f"[{saat}] [+] Requests Kütüphanesi Yüklendi ✔️")
            #download ip2geotools library for linux
            os.system("pip install ip2geotools")
            print(f"[{saat}][+] ip2geotools Kütüphanesi Yüklendi ✔️")
            #dowload colorama library for linux
            os.system("pip install colorama")
            print(f"[{saat}] [+] Colorama KÜtüphanesi Yüklendi ✔️")
            #download sqlite library for linuz
            os.system("pip install pysqlite3")
            print(f"[{saat}] [+] SQLite Kütüphanesi Yüklendi ✔️ ")
            time.sleep(1)
            os.system("clear")
        except ImportError:
            print("[+] Bu Program Python3 sürümü İle Çalışır Lütfen Güncelleyin")
            os.system("python --version")
            exit()

    if system() == "Windows":
        try:
            #download SpeechRecognition  library for windows
            os.system("pip install SpeechRecognition")
            print(f"[{saat}][+] Speech Recognition Kütüphanesi Yüklendi ✔️")
            #download gtts library for windows
            os.system("pip install gtts")
            print(f"[{saat}][+] GTTS Kütüphanesi Yüklendi ✔️")
            #download playsound library for windows
            os.system("pip install playsound")
            print(f"[{saat}][+] Playsound Kütüphanesi Yüklendi ✔️")  
            #download requests library for windows
            os.system("pip3 install requests")
            print(f"[{saat}][+] Requests Kütüphanesi Yüklendi ✔️")
            #download ip2geotools library for windows
            os.system("pip install ip2geotools")
            print(f"[{saat}][+] ip2geotools Kütüphanesi Yüklendi ✔️")
            #download colorama library for windows
            os.system("pip install colorama")
            print(f"[{saat}][+] Colorama Kütüphanesi Yüklendi ✔️")
            #download sqlite library for winows
            os.system("pip install pysqlite3")
            print(f"[{saat}][+] SQLite Kütüphanesi Yüklendi ✔️ ")
            time.sleep(1)
            os.system("cls")
        except ImportError:
            print("[+] Bu Program Python3 sürümü İle Çalışır Lütfen Güncelleyin")
            os.system("python --version")
            exit()

    print(f"[{saat}][+] Yükleme ve Kurulum Tamamlandı. Güle Güle Kullanın ... 😊")
    çalıştırma_inputu = input(f"[{saat}][+] Programı Çalıştırmak İstermisiniz (yes/no) :")
    if çalıştırma_inputu=="yes:" or çalıştırma_inputu=="YES":
        if system()=="Linux":
            ani()
            os.system("python main.py")
        if system()=="Windows":
            ani()
            os.system("python main.py")
            
    if çalıştırma_inputu == "no" or çalıştırma_inputu =="NO":
        if system()=="Windows":
            os.system("clear")
        if system()=="Windows":
            os.system("cls")
        print(f"[{saat}][+] Eğer İsterseniz (python main.py) Komutunu Çalıştırmanız Yeterli . Görüşürüz Çünkü Tekrar Görüşmek Zorundasın 😊 ")
    else:
        print(f"[{saat}][!] Lütfen Geçerli Bir Seçenek Giriniz .")
#// setup option menu
print("[+] 👾Sesli Asistana Hoşgeldiniz👾 ")
print("[+] Programı Kurmak İçin ( 1 ) Tuşuna Basın.")
print("[+] Programla İlgili Detayları Almak İçin ( 2 ) Tuşuna Basın ")
print("[+] Programı Kapatmak İçin ( 3 ) Tuşuna Basın ")
#Starting animation
a=input("Lütfen Seçeneği Girin = ")
def ani():
    print("[+] Program Çalıştırılıyor :")
    animation = ["■□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")
#Closing animation
def program_kapa_ani():
    print("[+] Program Kapatılıyor :")
    animation = ["■□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n") 
if a=="1":
    package()
#start about file
elif a=="2":
    print("[+] Detaylar Açılıyor .")
    if system()== "Linux":
        os.system("cat ABOUT.txt")
    if system()=="Windows":
        about_file = open("ABOUT.txt", encoding="utf-8")
        read_about_file = about_file.read()
        print(read_about_file)
#kapama animasyonu
elif a=="3":
    program_kapa_ani()
    exit()
else:
    print("[+] Düzgün Bir Şey Girer Misin ? Yoksa asistan üzülür .")

 
