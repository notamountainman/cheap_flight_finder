from twilio.rest import Client


def send_sms(destination_cities: list[tuple], twilio_acct: str, twilio_token: str, trips: list[tuple],
             twilio_number: str, personal_number: str) -> str:
    for count, trip_data in enumerate(trips):
        if trip_data[0] <= destination_cities[count][1]:
            client = Client(twilio_acct, twilio_token)
            message_body = f"Low Price Alert! Only ${trip_data[0]} to fly from {trip_data[1]}-{trip_data[2]} to " \
                           f"{trip_data[3]}-{trip_data[4]} from {trip_data[5]} to {trip_data[6]}. Airline(s) " \
                           f"{trip_data[7]}"
            message = client.messages.create(
                from_=twilio_number,
                body=message_body,
                to=personal_number
            )
            return message.sid
