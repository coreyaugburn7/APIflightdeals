

API_KEY = "GegrSS2HMkxTLUBLnFLE84vO__e0qCEf"
Tequila_endpoint = "https://tequila-api.kiwi.com"

#kiwi iata finder
kiwi_header = {
    "apikey": API_KEY,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = API_KEY
        self.tequila_endpoint = Tequila_endpoint
        self.kiwi_header = kiwi_header









