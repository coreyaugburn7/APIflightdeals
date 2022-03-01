import requests

Bearer_Authentication = "1Superuser!"

sheety_endpoint = "https://api.sheety.co/e724c33c0d78cff0d4cf5f72f6a1285c/copyOfFlightDeals/prices"

sheety_put_endpoint = f"https://api.sheety.co/e724c33c0d78cff0d4cf5f72f6a1285c/copyOfFlightDeals/prices/{id}"

headers = {
	"Authorization": f"Bearer {Bearer_Authentication}",
	"Content-Type": "application/json",
}

# The correct date format is dd/mm/YYYY, e.g. 29/05/2021

#sheet city puller data
search = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.bearer_auth = Bearer_Authentication
        self.sheety_endpoint = sheety_endpoint
        self.sheety_put = sheety_put_endpoint
        self.sheety_headers = headers


    def sheety_city_puller(self,):
        # response = requests.get(sheety_endpoint, headers=headers)
        # search = response.json()


        # city = search["prices"]
        # print(city)

        for n in search["prices"]:
            city = n["city"]
            print(city)

        return search











