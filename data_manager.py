import os
import pandas as pd
import requests

from flight_search import FlightSearch

class DataManager:
    def __init__(self):
        self.flight_data = self.getDataFrame()

    def putIataInRow(self, IATACode, row_idx):
        self.flight_data.loc[row_idx, "iataCode"] = IATACode
        return self.flight_data

    def getDataFrame(self):
        try:
            flight_data = pd.read_csv("flight_data.csv")
        except FileNotFoundError:
            data = {'city': ["Paris", "Berlin", "Tokyo", "Sydney", "Istanbul", "Kuala Lumpur", "New York",
                             "San Francisco", "Cape Town", "Uralsk"],
                    'iataCode': ["", "", "", "", "", "", "", "", "", ""],
                    'lowestPrice': [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]}
            flight_data = pd.DataFrame(data)
            flight_data.iataCode = flight_data.iataCode.astype(str)
        return flight_data

    def saveDataFrame(self):
        self.flight_data.to_csv("flight_data.csv", index=False)