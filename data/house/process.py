import json

merged = []

with open("./failed.json") as f:
	failed = json.load(f)
	merged += failed

with open("./listed_building.json") as f:
	data = json.load(f)
	merged += data["921"]
	merged += data["331"]

with open("./houses.json", "w") as f:
	json.dump(merged, f, ensure_ascii=False)
