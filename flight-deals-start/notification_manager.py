import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, price, departure_city, departure_code, arrival_city, arrival_code,
                     outbound_date, inbound_date):
        price = price
        departure_city = departure_city
        departure_code = departure_code
        arrival_city = arrival_city
        arrival_code = arrival_code
        outbound_date = outbound_date
        inbound_date = inbound_date

        account_sid = "AC396a9d9daa73cddebe1433853fb755bd"
        auth_token = "fdc0304693d5cb8248ffecf8c0623f06"
        client = Client(account_sid, auth_token)

        message = client.messages \
                                .create(
                                body= f"Only {price} to fly from {departure_city}-{departure_code} "
                                      f"to {arrival_city}-{arrival_code} from {outbound_date} to "
                                      f"{inbound_date}.",
                                from_="+16072846531",
                                to= "+17577130515"
        )

        print(message.body)











