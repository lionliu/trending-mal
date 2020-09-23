import pandas as pd
import numpy as np
from get_from_jikan import get_content

animeList = pd.read_csv("../data/anime/animes.csv")
animeList = animeList[:10]
newDataSet = get_content(animeList["uid"])
newDataSet = pd.DataFrame(newDataSet)
newDataSet.to_csv("../data/anime/newAnimes.csv", index=False)