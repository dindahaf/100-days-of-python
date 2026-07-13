import requests
import datetime as dt

MY_LAT = -6.175110
MY_LONG = 106.865036

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng":MY_LONG
}

response = requests.get(url="https://api.sunrise-sunset.org/v2", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = (data["sunrise"]).split("T")[1].split(":")[0]
sunset = (data["sunset"]).split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now.hour)