import json
import time
from urllib.request import Request, urlopen
from tqdm import tqdm

def get_field(field,obj,dataReturn):
    if field in obj:
        dataReturn[field].append(obj[field])
    else:
        dataReturn[field].append(0)

def get_multi_field(field,obj,dataReturn):
    if field in obj:
        dataReturn[field].append([s["name"] for s in obj[field]])
    else:
        dataReturn["studio"].append([])

def get_content(animeId):
    dataReturn = {
        "mal_id" : [],
        "title" : [],
        "studios" : [],
        "genres" : [],
        "source" : [],
        "rank" : [],
        "score" : [],
        "popularity" : [],
        "members" : [],
        "favorites" : [],
        "episodes" : []
    }
    for uid in tqdm(animeId):
        try:
            request = Request('https://api.jikan.moe/v3/anime/' + str(uid))
            response_body = urlopen(request).read()
            obj = json.loads(response_body)
            dataReturn["mal_id"].append(uid)
            get_field("title",obj,dataReturn)
            get_multi_field("studios",obj,dataReturn)
            get_multi_field("genres",obj,dataReturn)
            get_field("source",obj,dataReturn)
            get_field("rank",obj,dataReturn)
            get_field("score",obj,dataReturn)
            get_field("popularity",obj,dataReturn)
            get_field("members",obj,dataReturn)
            get_field("favorites",obj,dataReturn)
            get_field("episodes",obj,dataReturn)
        except:
            pass
        time.sleep(4)
    return (dataReturn)

#print( get_content([28891,2265,34599,35849]) )