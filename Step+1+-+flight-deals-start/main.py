#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# =========== keep the cache of the API so that we do not getting new API resource since the API is free plan and have limited requests ===========
import requests_cache

requests_cache.install_cache(
    cache_name="flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# load the environment variable inside the .env file
load_dotenv()

# set the date to apply it in the search of check flight
tomorrow = datetime.now() + timedelta(days=1)
print(tomorrow)
return_day = datetime.now() + timedelta(days=7)
print(return_day)

data_manager = DataManager()
sheet_data = data_manager.get_the_data()
pprint(sheet_data)

flight_search = FlightSearch()
notification_manager = NotificationManager()
# Looping the item in the sheet since we want to check several destinations
# check the flight using module in the FlightSearch class and getting the API response

ORIGIN_CITY_IATA = "CGK"
for destination in sheet_data:
    search_data = flight_search.check_flight(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=destination["iataCode"],
            from_date=tomorrow.strftime("%Y-%m-%d"),
            to_date=return_day.strftime("%Y-%m-%d"))
    pprint(search_data)


# Finding the cheapest flight from the API response

    cheapest_flight = find_cheapest_flight(search_data, return_day.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: IDR {cheapest_flight.price}")

# checking if the current price in the sheet are the lowest one, or it can find the lower price than that.
# if yes, then save it into the sheety sheet
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination['lowestPrice']:
        pprint(f"Lower price flight found to {sheet_data[2]['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        print("updated lowest price")
        notification_manager.send_whatsapp_message(
            text_message=f"Low price alert! Only IDR {cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )

