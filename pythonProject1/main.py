import requests
from datetime import datetime
# response = requests.get(url = 'http://api.open-notify.org/iss-now.json' )
# response.raise_for_status()#this raises an exeption based on if the api request returns an error.
#
# data = response.json()
# print(data)
#
# data = response.json()['iss_position'] #it works like a dictionary now
# print(data)
#
# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']
#
# iss_pos = longitude,latitude
# print(iss_pos)








lat = -43.532055
lng = 172.636230

sunrise_sunset_parameters = {
    'lat' : lat,
    'lng' : lng,
    'formatted': 0,
}

response = requests.get(url= 'https://api.sunrise-sunset.org/json', params= sunrise_sunset_parameters)
response.raise_for_status()
sun_times = response.json()
sunset = sun_times['results']['sunset']
sunrise = sun_times['results']['sunrise']

sunrise_time = [sunrise.split('T')[1].split(':')[0],sunrise.split('T')[1].split(':')[1]]
sunset_time = [sunset.split('T')[1].split(':')[0],sunset.split('T')[1].split(':')[1]]

now = datetime.now()
time_now = (int(now.hour), int(now.minute))

time_now_in_mins = (time_now[0]*60)+time_now[1]
sunrise_in_mins = (int(sunrise_time[0])*60)+int(sunrise_time[1])
sunset_in_mins = (int(sunset_time[0])*60)+int(sunset_time[1])

if sunset_in_mins <= time_now_in_mins >= sunset_in_mins:
    print('its too bright out!')
else:
    print('its nighttime')