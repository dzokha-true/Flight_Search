# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from pprint import pprint
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import date, timedelta

DM = DataManager()
FS = FlightSearch()


# for index, row in DM.flight_data.iterrows():
#     DM.putIataInRow(row_idx=index, IATACode=FS.getIATACode(row["city"]))
DM.saveDataFrame()
whole_sheet_data = DM.getDataFrame()
answers = []
for row in whole_sheet_data["iataCode"]:
    something = FS.getFlightData(destination=row)
    answers.append(FlightData(something).decodeData())

print(answers)