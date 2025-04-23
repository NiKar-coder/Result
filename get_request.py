import sys
import requests


def get_request(server_address, params):
    response = requests.get(server_address, params)
    if not response:
        print(params)
        print("HTTP status:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    return response


def get_toponym(response):
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]
    ["featureMember"][0]["GeoObject"]
    return toponym


def get_lonlat(toponym):
    lonlat = toponym["Point"]["pos"]
    lon, lat = lonlat.split(" ")
    return lon, lat


def get_spn(toponym):
    lower = list(
        map(float, toponym["boundedBy"]["Envelope"]['lowerCorner'].split()))
    upper = list(
        map(float, toponym["boundedBy"]["Envelope"]['upperCorner'].split()))
    spn1 = str(abs(lower[0] - upper[0]))
    spn2 = str(abs(lower[1] - upper[1]))
    return spn1, spn2
