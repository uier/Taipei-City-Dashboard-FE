import json
from collections import defaultdict

regions = [
    "北投區",
    "士林區",
    "內湖區",
    "南港區",
    "松山區",
    "信義區",
    "中山區",
    "大同區",
    "中正區",
    "萬華區",
    "大安區",
    "文山區",
]
jsons = ["flood-110", "flood-111", "flood-112"]
features = []
chart_data = defaultdict(lambda: defaultdict(int))

for j in jsons:
    with open(f"./{j}.json") as f:
        d = json.load(f)
        for row in d["Result"]:
            keys = {"deep", "area", "year"}
            for k in keys:
                row[k] = int(float(row[k]))
            fs = json.load(open(f"./geojsons/{row['filename']}.geojson"))["features"]
            for feature in fs:
                feature["properties"] = row
                features.append(feature)
            chart_data[row["deep"]][row["region"]] += 1

chart_data2 = [{"name": f"{k} cm", "data": [chart_data[k][v] for v in regions]} for k in sorted(chart_data.keys())]
json.dump(
    {
        "type": "FeatureCollection",
        "features": features,
    },
    open("./floods.geojson", "w"),
    ensure_ascii=False,
)
json.dump({ "data": chart_data2}, open("./floods.json", "w"))
