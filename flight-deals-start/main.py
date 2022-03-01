#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

teq_endpoint = flight_search.tequila_endpoint
teq_api = flight_search.api_key

bearer_auth = data_manager.bearer_auth
sheety_endpoint = data_manager.sheety_endpoint
sheety_put = data_manager.sheety_put
sheety_headers = data_manager.sheety_headers

search = data_manager.sheety_city_puller()
print(search["prices"])

id = 1

for n in search["prices"]:
	id += 1
	location_endpoint = f"{teq_endpoint}/locations/query"
	headers = {"apikey": teq_api}
	query = {"term": n["city"], "location_types": "city"}

	kiwi_response = requests.get(url=location_endpoint, headers=headers, params=query)
	# print(kiwi_response.json())
	iata_code = kiwi_response.json()
	# iata_code = iata_response["locations"][0]["code"]
	# print(iata_code)

	sheet_input = {
		"price": {
			"iataCode": iata_code["locations"][0]["code"]
		}
	}
	# #sheets put      sheety_put_endpoint
	# response = requests.put(f"https://api.sheety.co/e724c33c0d78cff0d4cf5f72f6a1285c/copyOfFlightDeals/prices/{id}"
	# 						, json=sheet_input, headers=headers)
	# print(response.text)


#FLIGHT DATA

sease = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
					{'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
					{'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
					{'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
					{'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}, {'city': 'Bali', 'iataCode': '', 'lowestPrice': 501, 'id': 11}]}


response = requests.get(sheety_endpoint, headers=sheety_headers)
search = response.json()
sheety_data = search["prices"]



today_date = datetime(year=2022, month=1, day=19)
end_date = datetime(year=2022, month=6, day=20)
min_return_date = datetime(year=2022, month=1, day=26)
max_return_date = datetime(year=2022, month=6, day=13)
today_date.strftime("%d/%m/%Y")
# 29/05/2021

sheety_flight_id = 1

for n in sheety_data:
	sheety_flight_id += 1
	location_endpoint = f"{teq_endpoint}/v2/search"
	headers = {"apikey": teq_api}
	query = {"fly_from":"LHR",
			 "fly_to": n["iataCode"],
			 "date_from":today_date.strftime("%d/%m/%Y"),
			 "date_to": max_return_date.strftime("%d/%m/%Y"),
			 "return_from": min_return_date.strftime("%d/%m/%Y"),
			 "return_to": end_date.strftime("%d/%m/%Y"),
			 "flight_type": "round",
			 "curr": "GBP",
			 "one_for_city": 1,
			 }
	#query = {"term": n["city"], "location_types": "city"}

	kiwi_response = requests.get(url=location_endpoint, headers=headers, params=query)
	# print(kiwi_response.json())

	print(n["iataCode"])
	sheety_price = n["lowestPrice"]
	flight_response = kiwi_response.json()

	flight_data.flight_info(flight_response, sheety_price)




