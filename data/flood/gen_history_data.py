import json
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from collections import defaultdict


@dataclass
class Flood:
    idx: str
    year: int
    region: str
    descript: str
    deep: float
    area: int
    type: str
    filename: str
    status: str
    datafrom: str
    reason: str
    station: str
    station_name: str
    create_dt: datetime
    occur_dt: datetime


raw_files = [
    "flood-110.json",
    "flood-111.json",
    "flood-112.json",
]
raw_floods: list[Flood] = []
parse_occur_at = lambda raw: datetime(
    int(raw.split("/")[0]),
    int(raw.split("/")[1]),
    int(raw.split("/")[2]),
    tzinfo=timezone(timedelta(hours=8)),
)
for fn in raw_files:
    raw_floods.extend(
        Flood(
            occur_dt=parse_occur_at(it.pop("occur_dt")),
            **it,
        )
        for it in json.load(open(fn))["Result"]
    )
# print(len(raw_floods))

history_data = defaultdict(int)
for flood in raw_floods:
    history_data[flood.occur_dt.isoformat()] += 1
history_data = [{"x": k, "y": v} for k, v in sorted(history_data.items())]
json.dump(
    {"data": [{"name": "", "data": history_data}]}, open("floods-history.json", "w")
)

# print(history_data)
