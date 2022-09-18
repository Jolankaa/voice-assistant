# Title: Weather Forecast
# Date: 2022-08-10
# Author: jolanka
# Category: Helpful For life Software
# Version: 1.01
#
import feedparser
import playsound
import os
from gtts import *
# locCode=EUR|TR|06420|ANKARA| > KITA|ULKE|POSTAKODU|IL 

def hava():
    #parametres
    istanbul="34764|İSTANBUL|"
    ankara="06420|ANKARA|"
    parse = feedparser.parse(f"http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|{istanbul}")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    print (parse[2], parse[4], parse[5])
    return (hava)

hava()