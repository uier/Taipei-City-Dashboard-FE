import json
from collections import defaultdict

data = json.load(open('./fire_hydrant_location.geojson'))

counter = defaultdict(int)
filtered_features = []

for row in data["features"]:
	if row["properties"]["location"][0] == "新":
		continue
	counter[row["properties"]["location"][3:6]] += 1
	row["properties"]["dist"] = row["properties"]["location"][3:6]
	filtered_features.append(row)

data["features"] = filtered_features

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
chart_data = []

for v in regions:
    chart_data.append(counter[v])

json.dump(
    data,
    open("./fire_hydrant_location_cluster.geojson", "w"),
    ensure_ascii=False,
)
json.dump(
    {
        "data": [
            {"name": "消防栓", "data": chart_data},
        ]
    },
    open("./153.json", "w"),
    ensure_ascii=False,
)


