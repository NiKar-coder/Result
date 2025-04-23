import sys
import io
from PIL import Image
from get_request import get_request, get_lonlat, get_toponym


geocode = ' '.join(sys.argv[1:])
server_address = 'http://geocode-maps.yandex.ru/1.x/'
api_key = '8013b162-6b42-4997-9691-77b7074026e0'
params = {
    "apikey": api_key,
    "geocode": geocode,
    "format": "json"
}
response = get_request(server_address, params)
toponym = get_toponym(response)
lon, lat = get_lonlat(toponym)


server_address = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
search_text = "аптека"
params = {
    "apikey": api_key,
    "text": search_text,
    "lang": "ru_RU",
    "ll": ','.join([str(i) for i in [lon, lat]]),
    "results": 10,
    "format": "json"}

response = get_request(server_address, params)
json_response = response.json()
orgs = json_response["features"]

org_marks = []
for org in orgs:
    org_ll = org["geometry"]["coordinates"]
    try:
        org_worktime = org["properties"]["CompanyMetaData"]
        ["Hours"]["Availabilities"][0]
    except KeyError:
        org_marks.append(",".join(map(str, org_ll)) + ",pm2grm")
    else:
        if "TwentyFourHours" in org_worktime:
            org_marks.append(",".join(map(str, org_ll)) + ",pm2gnm")
        else:
            org_marks.append(",".join(map(str, org_ll)) + ",pm2blm")


server_address = "http://static-maps.yandex.ru/1.x/"
params = {
    "l": "map",
    "pt": "~".join(org_marks)
}
response = get_request(server_address, params)
Image.open(io.BytesIO(response.content)).show()
