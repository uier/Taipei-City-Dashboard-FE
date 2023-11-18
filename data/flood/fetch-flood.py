import json
import requests

years = ["110", "111"]
data_root = "./kmls"

for y in years:
    with open(f"./flood-{y}.json", "r") as f:
        d = f.read()
        d = json.loads(d)

    floods = d["Result"]

    for f in floods:
        url = f"https://heovcenter.gov.taipei/TpeFloodRecord/kmlfile/taipeiflow/{f['filename']}.kml"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{data_root}/{f['filename']}.kml", "wb") as file:
                file.write(response.content)
                print(f"File {f['filename']}.kml downloaded successfully.")
        else:
            print(f"Failed to download file {f['filename']}.kml")
    
