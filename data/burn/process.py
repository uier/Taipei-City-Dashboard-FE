import csv
import json
from dataclasses import dataclass, asdict
from collections import defaultdict
from datetime import datetime, timezone, timedelta


@dataclass
class Burn:
    date: datetime
    month_occur_cnt: int


csv_name = "ps00036mc.csv"
raw_data = csv.DictReader(open(csv_name))
burn_datas: list[Burn] = []
today = datetime.now(tz=timezone(timedelta(hours=8)))

for burn in raw_data:
    year, month = map(int, burn["年月別"].rstrip("月").split("年"))
    year += 1911
    burn_date = datetime(year, month, day=1, tzinfo=timezone(timedelta(hours=8)))

    if today - burn_date > timedelta(days=730):
        continue

    new_burn = Burn(
        date=burn_date,
        month_occur_cnt=int(burn["火災發生次數[次]"]),
    )

    burn_datas.append(new_burn)

burn_datas = [
    {"x": b.date.isoformat(), "y": b.month_occur_cnt}
    for b in sorted(burn_datas, key=lambda b: b.date)
]
json.dump(
    {
        "data": [
            {"name": "每月火災發生次數", "data": burn_datas},
        ]
    },
    open("./burn.json", "w"),
    ensure_ascii=False,
)
