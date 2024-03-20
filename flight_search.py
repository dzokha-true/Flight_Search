import os
import requests
from pprint import pprint

API_ADDRESS = "https://api.tequila.kiwi.com/"
TEQUILA = os.environ["TEQUILA_API_KEY"]

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, icity="Boston"):
        self.icity = icity
        self.TEQUILA_API = TEQUILA
        self.apiAddress = API_ADDRESS + "locations/query";



    def getIATACode(self, city):
        params = {"term": city, "location_types": "city"}
        iata_code = requests.get(url=self.apiAddress, headers={"apikey": TEQUILA}, params=params)
        IataCode = iata_code.json()["locations"][0]["code"]
        return IataCode