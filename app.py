import requests

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


