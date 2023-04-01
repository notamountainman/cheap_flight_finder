from twilio.rest import Client


class NotificationManager():
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        pass

    def send_sms(self, destination_cities, twilio_acct, twilio_token, trips, twilio_number, personal_number):
        for item_number in range(len(trips)):
            if trips[item_number][0] <= destination_cities[item_number][1]:
                client = Client(twilio_acct, twilio_token)
                message_body = f"Low Price Alert! Only ${trips[item_number][0]} to fly from {trips[item_number][1]}-" \
                               f"{trips[item_number][2]} to {trips[item_number][3]}-{trips[item_number][4]} from " \
                               f"{trips[item_number][5]} to {trips[item_number][6]}. Airline(s) {trips[item_number][7]}"
                message = client.messages.create(
                    from_=twilio_number,
                    body=message_body,
                    to=personal_number
                )
                print(message.sid)
