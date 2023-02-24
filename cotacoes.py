# import requests

# api_key = 'f4f5066e95msha291532264445a2p115225jsnc9229cf97602'
symbol= 'BBAS3.SA'

# response = requests.get(f'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data?frequency=1d&filter=history&period1=1577836800&period2=1609459200&symbol={symbol}',
# headers={"X=RapidAPI-Key": api_key})

# if response.status_code == 200:
#     data=response.json()

#     print(data)
# else:
#     print('erro')

import requests
import json

url = f'https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{symbol}'

headers = {
    "X-RapidAPI-Key": "f4f5066e95msha291532264445a2p115225jsnc9229cf97602",
    "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
datajson = response.json()
a1 = json.dumps(datajson)
data = json.loads(a1)

for item in data:
    print(item["ask"])
