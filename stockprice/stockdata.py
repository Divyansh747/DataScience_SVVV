#!/usr/bin/python
print("content-type: text/html")
print()

import requests
import json
import cgi

form = cgi.FieldStorage()

code = form.getvalue("code")
url = "https://stock-price4.p.rapidapi.com/price/"+code

headers = {
    'x-rapidapi-key': "fc0425bf70msh0636f7cb69d4317p10d819jsn3af1691643bb",
    'x-rapidapi-host': "stock-price4.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

json_data = json.loads(response.text)

print("<center><b>")
print("<br><h1>"+json.dumps(json_data['shortName'])+"</h1>")
print("<br>regularMarketPreviousClose: "+json.dumps(json_data['regularMarketPreviousClose']))
print("<br>preMarketPrice: "+json.dumps(json_data['preMarketPrice']))
print("<br>marketState: "+json.dumps(json_data['marketState']))
print("<br>exchangeDataDelayedBy: "+json.dumps(json_data['exchangeDataDelayedBy']))
print("<br>Change: "+json.dumps(json_data['Change']))
print("<br>regularMarketPrice: "+json.dumps(json_data['regularMarketPrice']))
print("<br>preMarketChangePercent: "+json.dumps(json_data['preMarketChangePercent']))
print("<br>postMarketChangePercent: "+json.dumps(json_data['postMarketChangePercent']))
print("<br>Price: "+json.dumps(json_data['Price']))
print("<br>symbol: "+json.dumps(json_data['symbol']))
print("<br>regularMarketChange: "+json.dumps(json_data['regularMarketChange']))
print("<br>IsActive: "+json.dumps(json_data['IsActive']))
print("<br>regularMarketChangePercent: "+json.dumps(json_data['regularMarketChangePercent']))
print("<br>regularMarketOpen: "+json.dumps(json_data['regularMarketOpen']))
print("<br>shortName: "+json.dumps(json_data['shortName']))
print("<br>preMarketChange: "+json.dumps(json_data['preMarketChange']))
print("<br>regularMarketDayRange: "+json.dumps(json_data['regularMarketDayRange']))
print("<br>IsRegularTradingSession: "+json.dumps(json_data['IsRegularTradingSession']))
print("<br>postMarketPrice: "+json.dumps(json_data['postMarketPrice']))
print("<br>ChangePercent: "+json.dumps(json_data['ChangePercent']))
print("<br>currency: "+json.dumps(json_data['currency']))
print("<br>postMarketChange: "+json.dumps(json_data['postMarketChange']))
print("<br>fullExchangeName: "+json.dumps(json_data['fullExchangeName']))
print("</b></center>")

