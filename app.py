from rich.console import Console
from rich.table import Table
import requests
import os

root_url = "https://data.moenv.gov.tw"
query_url = "/api/v2/aqx_p_432"

data = {
    "api_key": "e8dd42e6-9b8b-43f8-991e-b3dee723a52d",
    "limit": 1000,
    "sort": "ImportDate desc",
    "format": "JSON"
}

res = requests.get(root_url + query_url, data)
data = res.json()

fields = data["fields"]
resource_id = data["resource_id"]
__extras = data["__extras"]
include_total = data["include_total"]
total = data["total"]
resource_format = data["resource_format"]
limit = data["limit"]
offset = data["offset"]
_links = data["_links"]
records = data["records"]

menu_field_id = ["sitename", "county", "aqi", "pollutant", "status"]


def field_name(id):
    for f in fields:
        if f["id"] == id:
            return f["info"]["label"]


def field_type(id):
    return fields[id]["type"]


def all_rec():
    t = Table(title="All Records")

    for field in fields:
        if field["id"] in menu_field_id:
            t.add_column(field_name(field["id"]))

    for record in records:
        status_color = "#fafafa"
        if record["status"] == "良好":
            status_color = "#16a34a"
        elif record["status"] == "普通":
            status_color = "#facc15"
        elif record["status"] == "對敏感族群不健康":
            status_color = "#f97316"
        elif record["status"] == "對所有族群不健康":
            status_color = "#ef4444"

        t.add_row(record["sitename"], record["county"],
                  record["aqi"], record["pollutant"], "["+status_color+"]"+record["status"]+"[/"+status_color+"]")
        pass

    console = Console()
    console.print(t)


def filte():
    county = []

    for r in records:
        if r["county"] not in county:
            county.append(r["county"])

    for i in range(len(county)):
        print(i, county[i])

    n = int(input("輸入縣市編號: "))

    if n < 0 or n >= len(county):
        quit()
        return

    for i in range(len(records)):
        if county[n] in records[i]["county"]:
            print(i, records[i]["sitename"], records[i]
                  ["aqi"], records[i]["pollutant"], records[i]["status"])

    num = int(input("輸入站點編號: "))

    for i in records[i].items():
        print(i)
        pass

    os.system("PAUSE")
    print(chr(27) + "[2J")


while True:
    filte()
