import os
import pprint
try:
    import requests
except ModuleNotFoundError:
    print("Requests 沒有安裝")
    os.system("pip install requests")

try:
    import rich
except NotADirectoryError:
    print("Rich 沒有安裝")
    os.system("pip install rich")
finally:
    from rich.table import Table
    from rich.console import Console

print(chr(27) + "[2J")

console = Console()

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

    print("-------------------------")
    n = int(input("輸入縣市編號(-1 to quit): "))

    if n < 0 or n >= len(county):
        return

    for i in range(len(records)):
        if county[n] in records[i]["county"]:
            print(i, records[i]["sitename"], records[i]
                  ["aqi"], records[i]["pollutant"], records[i]["status"])

    print("-------------")
    num = int(input("輸入站點編號: "))

    for i in records[num].items():
        print(f"{field_name(i[0])}: {i[1]}")
        pass

    os.system("PAUSE")
    print(chr(27) + "[2J")


def rich_filte():
    county = []

    for r in records:
        if r["county"] not in county:
            county.append(r["county"])

    county_menu = Table(title="county")
    county_menu.add_column("選項")
    county_menu.add_column("縣市")

    for i in range(len(county)):
        county_menu.add_row(str(i), county[i])
        
    console.print(county_menu)

    print("-------------------------")
    n = int(input("輸入縣市編號(-1 to quit): "))

    if n < 0 or n >= len(county):
        return

    site_menu = Table(title="site")
    site_menu.add_column("選項")
    site_menu.add_column("測站名稱")
    site_menu.add_column("空氣品質指標")
    site_menu.add_column("空氣污染指標物")
    site_menu.add_column("狀態")
    
    for i in range(len(records)):
        if county[n] in records[i]["county"]:
            
            status_color = "#fafafa"
            if records[i]["status"] == "良好":
                status_color = "#16a34a"
            elif records[i]["status"] == "普通":
                status_color = "#facc15"
            elif records[i]["status"] == "對敏感族群不健康":
                status_color = "#f97316"
            elif records[i]["status"] == "對所有族群不健康":
                status_color = "#ef4444"
            
            site_menu.add_row(str(i), records[i]["sitename"], records[i]
                              ["aqi"], records[i]["pollutant"], "["+status_color+"]"+records[i]["status"]+"[/"+status_color+"]")
    
    console.print(site_menu)

    print("-------------")
    num = int(input("輸入站點編號: "))

    for i in records[num].items():
        print(f"{field_name(i[0])}: {i[1]}")
        pass

    os.system("PAUSE")
    print(chr(27) + "[2J")


def simple_app():
    while True:
        print(chr(27) + "[2J")
        print("===================")
        print("1. Response Info")
        print("2. Query Data")
        print("===================")
        opt = int(input("請輸入選項: "))
        if opt == 1:
            print(chr(27) + "[2J")

            d = data.copy()
            del d["fields"]
            del d["records"]
            pprint.pp(d, depth=2)

            os.system("PAUSE")
        elif opt == 2:
            print(chr(27) + "[2J")

            filte()
        else:
            pass


def rich_app():
    main_menu = Table(title="AQI Info")
    main_menu.add_column("選項")
    main_menu.add_column("選項說明")
    main_opt = ["Response Info", "Query Data"]
    for i in range(len(main_opt)):
        main_menu.add_row(str(i+1), main_opt[i])

    while True:
        print(chr(27) + "[2J")
        console.print(main_menu)
        opt = int(input("請輸入選項: "))
        if opt == 1:
            print(chr(27) + "[2J")

            d = data.copy()
            del d["fields"]
            del d["records"]
            pprint.pp(d, depth=2)

            os.system("PAUSE")
        elif opt == 2:
            print(chr(27) + "[2J")

            rich_filte()
        else:
            pass


rich_app()
