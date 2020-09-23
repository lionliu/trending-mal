import json
import time
from urllib.request import Request, urlopen
from tqdm import tqdm

def get_content(animeId):
    dataReturn = {
        "ranked" : [],
        "score" : [],
        "popularity" : [],
        "members" : [],
        "studios" : [],
        "source" : [],
        "favorites" : [] 
    }
    for uid in tqdm(animeId):
        try:
            request = Request('https://api.jikan.moe/v3/anime/' + str(uid))
            response_body = urlopen(request).read()
            obj = json.loads(response_body)
            if "rank" in obj:
                dataReturn["ranked"].append(obj["rank"])
            else:
                dataReturn["ranked"].append(0)
            if "score" in obj:
                dataReturn["score"].append(obj["score"])
            else:
                dataReturn["score"].append(0)
            if "popularity" in obj:
                dataReturn["popularity"].append(obj["popularity"])
            else:
                dataReturn["popularity"].append(0)
            if "members" in obj:
                dataReturn["members"].append(obj["members"])
            else:
                dataReturn["members"].append(0)
            if "studios" in obj:
                dataReturn["studios"].append([s["name"] for s in obj["studios"]])
            else:
                dataReturn["studio"].append([])
            if "source" in obj:
                dataReturn["source"].append(obj["source"])
            else:
                dataReturn["source"].append("")
            if "favorites" in obj:
                dataReturn["favorites"].append(obj["favorites"])
            else:
                dataReturn["favorites"].append(0)
        except:
            dataReturn["ranked"].append(0)
            dataReturn["score"].append(0)
            dataReturn["popularity"].append(0)
            dataReturn["members"].append(0)
            dataReturn["studios"].append([])
            dataReturn["source"].append("")
            dataReturn["favorites"].append(0)
        time.sleep(4)
    return (dataReturn)

print( get_content([28891,23273,34599,35849]) )