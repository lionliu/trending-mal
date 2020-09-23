import json
from urllib.request import Request, urlopen
from tqdm import tqdm

def get_content(animeId):
    apiLink = 'https://api.jikan.moe/v3/anime/'
    dataReturn = {
        "rank" : [],
        "score" : [],
        "popularity" : [],
        "members" : [],
        "studio" : [],
        "source" : [],
        "favorites" : [] 
    }
    for uid in tqdm(animeId):
        try:
            request = Request('https://api.jikan.moe/v3/anime/' + str(uid))
            response_body = urlopen(request).read()
            obj = json.loads(response_body)
            dataReturn["rank"].append(obj["rank"])
            dataReturn["score"].append(obj["score"])
            dataReturn["popularity"].append(obj["popularity"])
            dataReturn["members"].append(obj["members"])
            dataReturn["studio"].append([s["name"] for s in obj["studios"]])
            dataReturn["source"].append(obj["source"])
            dataReturn["favorites"].append(obj["favorites"])
        except:
            dataReturn["rank"].append(0)
            dataReturn["score"].append(0)
            dataReturn["popularity"].append(0)
            dataReturn["members"].append(0)
            dataReturn["studio"].append([])
            dataReturn["source"].append("")
            dataReturn["favorites"].append(0)
    return (dataReturn)

print( get_content([28891,23273,34599,35849]) )