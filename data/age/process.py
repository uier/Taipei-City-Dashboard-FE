import json

data = json.load(open("./building_age_picto.geojson"))

assert len(data["features"]) == len(list(filter(lambda x: x["properties"]["age_2021"], data["features"])))

chart_data = { "data": { "name": "每百棟房屋", "data": [0, 0, 0, 0] } }

for feature in data["features"]:
	age = feature["properties"]["age_2021"]
	if age > 40:
		chart_data["data"]["data"][0] += 1
	elif age > 20:
		chart_data["data"]["data"][1] += 1
	elif age > 5:
		chart_data["data"]["data"][2] += 1
	else:
		chart_data["data"]["data"][3] += 1

json.dump(chart_data, open("./155.json", "w"))


