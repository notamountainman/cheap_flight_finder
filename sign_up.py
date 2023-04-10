import requests
import time


class SignUp:

    def __init__(self):
        self.sheety_post_url = "https://api.sheety.co/"
        self.sheety_page = "/flightDeals/users/"
        self.perfect_user_entry = False

    def sign_up(self, sheety_token: str, sheety_sheet_id: str) -> None:
        while not self.perfect_user_entry:
            print("Welcome to Daniel's Flight Club!\nWe find the best flight deals and email you.")
            first_name = input("What is your first name?: ")
            last_name = input("What is your last name?: ")
            email = input("What is your email?: ")
            confirm_email = input("Type your email again.: ")
            if email == confirm_email:
                self.perfect_user_entry = True
            else:
                print("Sorry, email doesn't match! Please try again\n")
                time.sleep(2)

        sheety_header = {
            "Authorization": f"Bearer {sheety_token}"
        }
        sheety_body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        add_to_mailing_list = requests.post(url=f"{self.sheety_post_url}{sheety_sheet_id}{self.sheety_page}",
                                            headers=sheety_header, json=sheety_body)
        if add_to_mailing_list.raise_for_status() is None:
            print("Success! You've been added to the mailing list!")
