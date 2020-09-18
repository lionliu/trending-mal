import requests
from bs4 import BeautifulSoup

url = "https://myanimelist.net/anime/35849/Darling_in_the_FranXX?q=Darlin&cat=anime"


def get_content(url, content="Studios:"):
    html = requests.get(url).content
    soup = BeautifulSoup(html, features="html.parser")
    divStudio = soup.find('span', string=content).parent
    studios = divStudio.find_all('a')
    return [s.contents[0] for s in studios]

# print(get_content(url))
