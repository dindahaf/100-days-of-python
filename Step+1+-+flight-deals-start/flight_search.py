#This class is responsible for talking to the Flight Search API.
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["SERP_API_KEY"]
        self.api = "https://serpapi.com/search"

    def check_flight(self, origin_city_code, destination_city_code, from_date, to_date, is_direct=True):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_date,
            "return_date": to_date,
            "type": "1",
            "adults": "1",
            "currency": "IDR",
            "api_key": self._api_key,
        }

        # Only include stops parameter if is_direct is True
        if is_direct:
            query["stops"] = "1"

        flight_response = requests.get(url=self.api, params=query)

        if flight_response.status_code != 200:
            print(f"check_flights() response code: {flight_response.status_code}")
            return None

        data = flight_response.json()
        if "error" in data:
            print(f"API error: {data["error"]}")
            return None
        return data


