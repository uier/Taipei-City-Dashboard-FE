import csv
import json
from dataclasses import dataclass, asdict
from collections import defaultdict


@dataclass
class HospitalChartData:
    name: str
    address: str
    bed_count: int
    dist: str
    # 緯度
    latitude: float
    # 經度
    longitude: float


csv_name = "臺北市公私立醫院病床數統計.csv"
xy_csv_name = "台北市醫院清冊.csv"
raw_xy = list(csv.DictReader(open(xy_csv_name)))
raw_data = csv.DictReader(open(csv_name))
hospital_chart_datas: list[HospitalChartData] = []
features = []

for hospital in raw_data:
    dist = hospital["地址"][3:6]
    try:
        xy_row = next(xy for xy in raw_xy if hospital["機構名稱"] in xy["機構名稱"])
    except StopIteration:
        print(hospital)
        raise
    new_hospital = HospitalChartData(
        name=hospital["機構名稱"],
        address=hospital["地址"],
        bed_count=int(hospital["急性一般病床數"]),
        dist=dist,
        latitude=float(xy_row["y"]),
        longitude=float(xy_row["x"]),
    )

    hospital_chart_datas.append(new_hospital)
    features.append(
        {
            "type": "Feature",
            "properties": asdict(new_hospital),
            "geometry": {
                "type": "Point",
                "coordinates": [new_hospital.longitude, new_hospital.latitude],
            },
        }
    )

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
    bed_count = sum(h.bed_count for h in hospital_chart_datas if h.dist == v)
    chart_data.append(bed_count)

json.dump(
    {
        "type": "FeatureCollection",
        "features": features,
    },
    open("./hospitals.geojson", "w"),
    ensure_ascii=False,
)
json.dump(
    {
        "data": [
            {"name": "急性一般病床數", "data": chart_data},
            {"name": "dummy", "data": [0 for _ in regions]},
        ]
    },
    open("./hospitals.json", "w"),
    ensure_ascii=False,
)
