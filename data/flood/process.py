import json

jsons = ["flood-110", "flood-111", "flood-112"]
data = []

for j in jsons:
	with open(f"./{j}.json") as f:
		d = json.load(f)
		for row in d["Result"]:
			data.append(row)
			

f = open("./floods.json", "w")
json.dump(data, f, ensure_ascii=False)
