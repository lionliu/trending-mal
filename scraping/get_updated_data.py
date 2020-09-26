import pandas as pd
import numpy as np
from get_from_jikan import get_content

animeList = pd.read_csv(r'./animes.csv')
# animeList = animeList[9655:-1]
newDataSet = get_content(animeList["uid"])
newDataSet = pd.DataFrame(newDataSet)
newDataSet.to_csv(r'./newAnimes.csv', index=False)