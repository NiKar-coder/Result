import sys
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

server_address = 'http://geocode-maps.yandex.ru/1.x/'
api_key = '8013b162-6b42-4997-9691-77b7074026e0'

params = {
    "apikey": api_key,
    "kind": "district",
    "lang": "ru_RU",
    "geocode": ','.join([str(i) for i in [lon, lat]]),
    "format": "json"}

response = get_request(server_address, params)

toponym = get_toponym(response)
district = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
print(district)
