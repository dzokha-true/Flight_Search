import os
import requests
from datetime import date, timedelta
from pprint import pprint

API_ADDRESS = "https://api.tequila.kiwi.com/"
TEQUILA = os.environ["TEQUILA_API_KEY"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, icity="Boston"):
        self.icity = icity
        self.TEQUILA_API = TEQUILA
        self.apiAddress = API_ADDRESS + "locations/query";

    def getIATACode(self, city):
        params = {"term": city, "location_types": "city"}
        iata_code = requests.get(url=self.apiAddress, headers={"apikey": TEQUILA}, params=params)
        IataCode = iata_code.json()["locations"][0]["code"]
        return IataCode

    def getFlightData(self, destination, date_from=date.today().strftime("%d/%m/%Y"),
                      date_to=(date.today() + timedelta(days=180)).strftime("%d/%m/%Y"), hand_bags=1): #TODO consider return iteneraries as well.
        origin = self.icity
        data = {"fly_from": f"BOS", "fly_to": f"{destination}", "dateFrom": date_from, "dateTo": date_to,
                "adault_hold_bag": f"{hand_bags}"}
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers={"apikey": TEQUILA}, params=data)
        print(response)
        return response.json()
