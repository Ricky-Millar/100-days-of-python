import smtplib
from datetime import datetime
import time
import requests

LAT = -43.532055
LNG = 172.636230
POS_VARI = 5  # range from user lng and lat that the iss will report as being visable eg 13 +/- 5 = range of 8-18
UTC_OFFSET = 12
MY_EMAIL = "rickysemailforpythonprojects@gmail.com"


def iss_above():
    global POS_VARI, LAT, LNG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if LAT - POS_VARI <= iss_latitude <= LAT + POS_VARI and LNG - POS_VARI <= iss_longitude <= LNG + POS_VARI:
        print('isis overhead')
        return True
    else:
        print('isis far away')
    return False


def utc_to_local(time):
    global UTC_OFFSET
    time += UTC_OFFSET
    if time > 23:
        time -= 24
    return time


def dark_enough():
    global LAT, LNG
    # Format data for API request
    sunrise_sunset_parameters = {
        'lat': LAT,
        'lng': LNG,
        'formatted': 0,
    }
    # get data from API
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=sunrise_sunset_parameters)
    response.raise_for_status()
    sun_times = response.json()
    sunset = sun_times['results']['sunset']
    sunrise = sun_times['results']['sunrise']
    # format data into a list of int,s [hour, min] in UTC time
    sunrise_time = [int(sunrise.split('T')[1].split(':')[0]), int(sunrise.split('T')[1].split(':')[1])]
    sunset_time = [int(sunset.split('T')[1].split(':')[0]), int(sunset.split('T')[1].split(':')[1])]
    # get current time
    now = datetime.now()
    time_now = [int(now.hour), int(now.minute)]
    # convert hours from UTC time to local time
    sunset_time[0] = utc_to_local(sunset_time[0])
    sunrise_time[0] = utc_to_local(sunrise_time[0])
    # Debug - print(sunset_time, sunrise_time)
    time_now_in_mins = (time_now[0] * 60) + time_now[1]
    sunrise_in_mins = (sunrise_time[0] * 60) + sunrise_time[1]
    sunset_in_mins = (sunset_time[0] * 60) + sunset_time[1]
    # DEBUG - print(f'sunset:{sunset_in_mins},sunrise:{sunrise_in_mins},time now:{time_now_in_mins}')
    # Return true if it is dark enough to see the ISS, eg it is nighttime.
    if sunrise_in_mins <= time_now_in_mins and time_now_in_mins <= sunset_in_mins:
        print('its too bright out!')
        return False
    else:
        print('its nighttime')
        return True


def send_mail():
    with smtplib.SMTP('smtp.gmail.com',
                      587) as connection:  # new object SMTP from the smtplib library, the smtp.gmail.com is the service we are connecting too.

        connection.starttls()  # TLS = Transport layer security, it is encryption for the connection
        connection.login(user=MY_EMAIL, password='abcd1234()###')
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='ricky.j.millar@gmail.com',
                            msg=f'Subject: ISS Alert!\n\nISS IS OVERHEAD!'
                            )

while True:
    time.sleep(60)
    if dark_enough() and iss_above():
        send_mail()
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
