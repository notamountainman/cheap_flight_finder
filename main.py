from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import send_sms
from sign_up import SignUp
import os

SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
SHEET_ID = os.environ.get('SHEET_ID')
TEQUILA_TOKEN = os.environ.get('TEQUILA_TOKEN')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_ACCT = os.environ.get('TWILIO_ACCT')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
PERSONAL_NUMBER = os.environ.get('PERSONAL_NUMBER')

TAKEOFF_LOCATION_CODE = "LAX"

mailing_list = SignUp()
mailing_list.sign_up(SHEETY_TOKEN, SHEET_ID)

data_manager = DataManager()
sheet_data = data_manager.sheety_api_get(SHEETY_TOKEN, SHEET_ID)

cities = []
for row in sheet_data['prices']:
    cities.append((row['city'], row['lowestPrice']))

flight_search = FlightSearch()
flight_search_post = flight_search.sheet_api_push(SHEETY_TOKEN, TEQUILA_TOKEN, SHEET_ID, cities)

flight_data = FlightData()
flight_data_get = flight_data.get_flights(TEQUILA_TOKEN, flight_search_post, TAKEOFF_LOCATION_CODE)

send_sms(cities, TWILIO_ACCT, TWILIO_TOKEN, flight_data_get, TWILIO_NUMBER,
         PERSONAL_NUMBER)
