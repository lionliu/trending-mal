import requests
from bs4 import BeautifulSoup

url = ["https://myanimelist.net/anime/35849/Darling_in_the_FranXX?q=Darlin&cat=anime","https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood"]


def get_content(url, content="Studios:"):#Url will be an object
  dataReturn = []
  for x in url:
    html = requests.get(x).content
    soup = BeautifulSoup(html, features="html.parser")
    try:
        divStudio = soup.find('span', string=content).parent
        studios = divStudio.find_all('a')
        aux = [s.contents[0] for s in studios]
        dataReturn.append(aux)
    except:
        dataReturn.append([])
    time.sleep(5)
  return dataReturn

print(get_content(url))
