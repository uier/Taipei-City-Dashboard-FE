import requests
import json
import re
from time import sleep

jsons = ["921", "331"]
data = {}

for j in jsons:
    f = open(f"{j}.json")
    d = f.read()
    d = json.loads(d)
    houses = d["data"]
    item = []
    for h in houses:
        url = f"https://www.google.com/maps/search/{h}"
        response = requests.get(url)
        match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', response.content.decode())
        if match:
            latitude = float(match.group(1))
            longitude = float(match.group(2))
            print(f"Latitude: {latitude}, Longitude: {longitude}, URL: {url}")
            item.append({
                "address": h,
                "lat": latitude,
                "lng": longitude
            })
        else:
            print(f"Failed to get location of {h}")
        sleep(1) # Avoid being blocked by Google
    data[j] = item

f = open("listed_building.json", "w")
f.write(json.dumps(data))
