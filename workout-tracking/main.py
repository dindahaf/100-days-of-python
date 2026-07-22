import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = 53
HEIGHT_CM = 164
AGE = 29

API_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

endpoint = "https://app.100daysofpython.dev"
post_endpoint = f"{endpoint}/v1/nutrition/natural/exercise"
sheety_endpoint = os.environ["SHEET_ENDPOINT"]

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

exercise_text = input("Tell me which exercises you did: ")

exercise_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=post_endpoint, json=exercise_data, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().date().strftime("%d/%m/%Y")
today_time = datetime.now().time().strftime("%H:%M:%S")
print(today_date)
print(today_time)


for item in result["exercises"]:
    print(len(result["exercises"])) # There is a bug in the API that makes we can't put more than one exercises in one input
    sheety_data = {}
    sheety_data = {
            "workout":{
                "date": today_date ,
                "time": today_time,
                "exercise": item["name"].title(),
                "duration": item["duration_min"],
                "calories": item["nf_calories"],
            }
        }
    sheet_response = requests.post(url=sheety_endpoint, json=sheety_data, headers=bearer_headers)
    print(sheet_response.text)

