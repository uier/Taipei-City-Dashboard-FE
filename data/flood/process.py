import json

jsons = ["flood-110", "flood-111", "flood-112"]
features = []

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


f = open("./floods.geojson", "w")
json.dump({
	"type": "FeatureCollection",
	"features": features,
}, f, ensure_ascii=False)
