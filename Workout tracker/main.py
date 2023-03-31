import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
AUTHORIZATION = os.environ["AUTHORIZATION"]
ENDPOINT_EXCEL = os.environ["ENDPOINT_EXCEL"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}
parameters = {
     "query": input("Tell me which exercise you did: "),
     "gender": "female",
     "weight_kg": 68,
     "height_cm": 168,
     "age": 46,
}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=endpoint, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
workout_data = data["exercises"]

today = datetime.now()

headers_data = {
    "Authorization": AUTHORIZATION,
}

for item in workout_data:
    workout_parameters = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }

    update = requests.post(url=ENDPOINT_EXCEL, json=workout_parameters, headers=headers_data)
print(update.text)
