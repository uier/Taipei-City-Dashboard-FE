import json

f = open("./houses.json")
data = json.load(f)

chartdata = {
	"data": {
		"name": "尚餘",
		"data": len(data)
	}
}

f = open("./150.json", "w")
json.dump(chartdata, f, ensure_ascii=False)
