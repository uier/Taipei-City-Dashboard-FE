import kml2geojson
import pathlib
import json

for path in pathlib.Path("./kmls").iterdir():
    d, *_ = kml2geojson.main.convert(path)
    with open(f"./geojsons/{path.stem}.geojson", "w") as f:
        json.dump(d, f)
        print(f"File {path.stem}.geojson converted successfully.")
