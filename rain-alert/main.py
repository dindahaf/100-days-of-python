import requests
from twilio.rest import Client

Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "563134a7b816b35d16181a3cb4f9f36f"
MY_LAT = 1.35
MY_LONG = 103.82
account_sid = "AC3461b488eda6e20a07bcc8d2b267fffa"
auth_token = "0c4aab5f2f0e5de61791601525dd82ea"


weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in range(4):
    condition_code = weather_data["list"][hour_data]["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+6282213861808",
    )

    print(message.status)

