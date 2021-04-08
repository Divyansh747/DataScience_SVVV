import requests
import json
import urllib.request
print(
'''
Name           :- Divyansh Rahangdale
Enrollment no. :- 18100BTCSES02782
'''
)

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"Delhi,in","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring).text
print(response)
