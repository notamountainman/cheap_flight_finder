import requests
from pprint import pprint
from datetime import datetime, timedelta


class FlightData:

    def __init__(self):
        self.base_url = "https://api.tequila.kiwi.com/v2/search"

    def get_flights(self, tequila_token, iata_code_list, airport):
        tomorrow = str(datetime.strftime((datetime.today() + timedelta(days=1)).date(), "%d/%m/%Y"))
        one_eighty_days = str(datetime.strftime((datetime.today() + timedelta(days=180)).date(), "%d/%m/%Y"))
        flight_search_url = f"{self.base_url}?date_from={tomorrow}&date_to={one_eighty_days}"
        tequila_header = {
            "apikey": tequila_token
        }
        best_deals = []
        for code in iata_code_list:
            tequila_parameters = {
                "fly_from": airport,
                "fly_to": code,
                "curr": "USD",
                "nights_in_dst_from": "4",
                "nights_in_dst_to": "14",
                "flight_type": "round"
            }

            response = requests.get(url=flight_search_url, headers=tequila_header, params=tequila_parameters)
            response.raise_for_status()
            all_flights = response.json()

            with open("all_flights.txt", "w") as file:
                pprint(all_flights, file)

            best_price = 5000
            for flight in all_flights['data']:
                if int(flight['price']) < best_price and flight['availability']['seats'] != "None":
                    best_price = flight['price']
                    departure_city = flight['cityFrom']
                    departure_city_code = flight['cityCodeFrom']
                    arrival_city = flight['cityTo']
                    arrival_city_code = flight['cityCodeTo']
                    airlines = flight['airlines']

                    utc_departure = flight['utc_departure'][0:10]
                    utc_arrival = flight['utc_arrival'][0:10]

                    arrival_date = datetime.strptime(utc_arrival, "%Y-%m-%d")
                    nights_in_dest = int(flight['nightsInDest'])
                    last_night = datetime.strftime(arrival_date + timedelta(days=nights_in_dest), "%Y-%m-%d")

            best_deals.append((best_price, departure_city, departure_city_code, arrival_city, arrival_city_code,
                               datetime.strftime(arrival_date, "%Y-%m-%d"), last_night, airlines))
        return best_deals
        # print(f"{all_flights['data'][0]['cityFrom']} to {all_flights['data'][0]['cityTo']}: "
        # f"${all_flights['data'][0]['price']}\n")
