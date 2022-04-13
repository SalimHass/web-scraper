import requests

URL = "https://en.wikipedia.org/wiki/Cape_Town"
res = requests.get(URL)

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.content, "html.parser")

