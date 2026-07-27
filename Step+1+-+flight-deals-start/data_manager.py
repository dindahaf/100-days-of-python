import os
import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_endpoint = os.environ["SHEET_ENDPOINT"]
        self.destinations = []
        self.bearer_headers = {
            "Authorization": f"Bearer {os.environ["TOKEN"]}"
        }

    def get_the_data(self):
        sheet_response = requests.get(url=self.sheet_endpoint)
        data = sheet_response.json()
        self.destinations = data["prices"]
        return self.destinations

    def update_lowest_price(self, row_id, new_price):
        new_data ={
            "price": {
                "lowestPrice": new_price
            }
        }
        update_response = requests.put(
            url=f"{self.sheet_endpoint}/{row_id}",
            json=new_data,
            headers=self.bearer_headers
        )




