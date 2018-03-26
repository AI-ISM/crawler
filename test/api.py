import json
from urllib.request import urlopen


def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read()
    responseJson = json.loads(response)
    return responseJson.get('country_name')

print(getCountry("39.108.132.71"))