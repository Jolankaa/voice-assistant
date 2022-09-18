import requests
from bs4 import BeautifulSoup

SELECTOR = "#mw-content-text > div.mw-parser-output > p:nth-child(3)"
URL = "https://tr.wikipedia.org/wiki/Futbol"

html = requests.get(
    URL,
    headers={
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58',
    }
).text.encode("utf-8")
soup = BeautifulSoup(html, "html.parser")
selected_element = soup.select_one(SELECTOR)
print(soup.get_text())