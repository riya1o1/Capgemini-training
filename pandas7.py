import json
import requests
import pandas as pd
from pandas import json_normalize
with open ('/content/raw_nyc_phil.json') as f:
    d = json.load(f)
nycphil = json_normalize(d['programs'])
nycphil.head(3)