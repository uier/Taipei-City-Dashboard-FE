1. manually download the jsons
2. run `fetch.py` to fetch the kmls based on filenames in jsons
3. run `convert.py` to convert kmls to geojsons
4. run `process.py` to merge jsons into one `floods.json`
5. NOTE THAT `flood-108.json` has been modified manually to fix the wrong date
   - `20190830_100010.kml` is corrupted, so it is removed from `flood-108.json`
6. a flood record with deep=18.00 has been removed in `flood-109.json`