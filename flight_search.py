import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.sheety_post_url = "https://api.sheety.co/"
        self.sheety_column = "/flightDeals/prices/"
        self.tequila_locations_url = "https://api.tequila.kiwi.com/locations/query/"
        self.city_codes = []

    def iata_search(self, tequila_token, current_city):
        tequila_header = {
            "apikey": tequila_token
        }
        tequila_params = {
            "term": current_city
        }
        code_search = requests.get(url=self.tequila_locations_url, headers=tequila_header, params=tequila_params)
        code_search.raise_for_status()
        formatted_search = code_search.json()
        return formatted_search["locations"][0]["code"]

    def sheet_api_push(self, sheety_token, tequila_token, sheety_sheet_id, cities):
        sheety_header = {
            "Authorization": f"Bearer {sheety_token}"
        }
        for row in range(len(cities)):
            city_iata = self.iata_search(tequila_token, cities[row][0])
            body = {
                "price": {
                    "city": cities[row][0],
                    "iataCode": city_iata
                }
            }
            sheety_post = requests.put(url=f"{self.sheety_post_url}{sheety_sheet_id}{self.sheety_column}{row + 2}",
                                       headers=sheety_header, json=body)
            sheety_post.raise_for_status()
            self.city_codes.append(city_iata)
        return self.city_codes
