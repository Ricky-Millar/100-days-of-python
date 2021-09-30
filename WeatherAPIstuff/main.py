import requests
import os

APIKEY = 'dbb81b3e50a84e5816a5bade15636f11'
ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
LAT = 43.576558
LONG = 172.635107
EXCLUSION_LIST = 'current,minutely,daily'
PARAMS = {
    'lat': LAT,
    'lon': LONG,
    'appid': APIKEY,
    'exclude': EXCLUSION_LIST
}

response = requests.get(url= ENDPOINT, params= PARAMS)
response.raise_for_status()
weather_data = response.json()

def umbrella_decider():
    bring_umbrella = False
    for i in range(12):
        ID = weather_data['hourly'][i]['weather'][0]['id']
        if ID <= 600:
            bring_umbrella = True
    return bring_umbrella

if umbrella_decider():
    print ('bring it bro')
else:
    print ('its nice out')