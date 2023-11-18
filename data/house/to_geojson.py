import json

f = open("./houses.json")
data = json.load(f)

geojson = {
	"type": "FeatureCollection",
	"features": []
}

for house in data:
	feature = {
		"type": "Feature",
		"properties": {
			"address": house["address"]
		},
		"geometry": {
			"type": "Point",
			"coordinates": [
				house["lng"],
				house["lat"]
			]
		}
	}
	geojson["features"].append(feature)

f = open("./earthquake_listed_houses.geojson", "w")
json.dump(geojson, f, ensure_ascii=False)
