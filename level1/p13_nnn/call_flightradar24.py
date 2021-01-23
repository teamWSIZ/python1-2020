from typing import Dict

import requests
from dataclasses import dataclass


@dataclass
class FlyingObject:
    lon: float
    lat: float
    track_deg: float
    altitude_ft: float
    ground_speed_kts: float


f = FlyingObject(58, 16, 180, 35000, 100)
# print(f)

url = 'https://data-live.flightradar24.com/zones/fcgi/feed.js?bounds=50.32,49.87,16.22,20.20'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

r = requests.get(url, headers=headers)
# print(r.json())
g: Dict = r.json()
for (k, v) in g.items():
    print(k,v)
#     if type(v) == type([]):
#         print(f'{k} -> {v}, {v[9]}')
