import requests


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.sheety_get_url = "https://api.sheety.co/"
        self.sheety_column = "/flightDeals/prices"

    def sheety_api_get(self, token, sheety_sheet_id):
        sheety_header = {
            "Authorization": f"Bearer {token}"
        }
        sheety_get = requests.get(url=f"{self.sheety_get_url}{sheety_sheet_id}{self.sheety_column}",
                                  headers=sheety_header)
        sheety_get.raise_for_status()
        return sheety_get.json()