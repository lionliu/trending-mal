from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'http://cin.ufpe.br/~llm2/anime.zip'
with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall()