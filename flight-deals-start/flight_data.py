from notification_manager import NotificationManager

noti_manager =NotificationManager()

class FlightData:
    #This class is responsible for structuring the flight data.
    def flight_info(self, flight_response, sheety_price):
        print(flight_response)
        for flight in flight_response["data"]:
            if sheety_price >= flight["price"]:
                price = flight["price"]
                departure_city = flight["cityFrom"]
                departure_code = flight["flyFrom"]
                arrival_city = flight["cityTo"]
                arrival_code = flight["cityCodeTo"]
                outbound_date = flight["local_departure"].split("T")[0]
                inbound_date = flight["route"][-1]["local_departure"].split("T")[0]


                print(arrival_city)
                print(sheety_price)
                print(price)
                print(departure_code)

                noti_manager.send_message(price, departure_city, departure_code, arrival_city, arrival_code,outbound_date, inbound_date)
















