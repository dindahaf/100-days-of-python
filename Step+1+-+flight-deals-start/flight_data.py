import requests

#This class is responsible for structuring the flight data.
class FlightData:

    def __init__(self, api_price, api_origin_airport, api_destination_airport, api_out_date, api_return_date):
        self.price = api_price
        self.origin_airport = api_origin_airport
        self.destination_airport = api_destination_airport
        self.out_date = api_out_date
        self.return_date = api_return_date

def find_cheapest_flight(api_data, return_date ):
    # Handle empty data if no flight data is returned
    if api_data is None or (not api_data.get("best_flights") and not api_data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    all_flights = api_data.get("best_flights",[]) + api_data.get("other_flights", [])

    # Getting the first flight's items from all_flights as the baseline for subsequent flight comparisons.
    first_flight = all_flights[0]
    lowest_price = first_flight["price"]
    origin = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    # Set the items for the FlightData class
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    # Looking for the lowest price from all_flight with looping all the flight
    for flight in all_flights:
        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price:
            lowest_price = price
            origin = first_flight["flights"][0]["departure_airport"]["id"]
            destination = first_flight["flights"][-1]["arrival_airport"]["id"]
            out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

            # if the price in this flight is the lowest one by the time this flight come up,
            # then assign all the necessary items to the FLightData class.
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is IDR {lowest_price}")
    return cheapest_flight

    # let's move to the main.py to process the function.

