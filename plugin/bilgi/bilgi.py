import requests
import wikipedia
from bs4 import BeautifulSoup

baslik = input("Başlığı Giriniz: ")
link = "https://tr.wikipedia.org/wiki/" + str(baslik.lower())
r = requests.get(link)
soup = BeautifulSoup(r.content, "lxml")
st1 = soup.find_all("div", attrs = {"id":"bodyContent"})
text = st1[0].text
print(text)