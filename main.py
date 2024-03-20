# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from pprint import pprint
import requests
from data_manager import DataManager
from flight_search import FlightSearch

DM = DataManager()
FS = FlightSearch()

whole_sheet_data = DM.getDataFrame()
print(whole_sheet_data)
for index, row in DM.flight_data.iterrows():
    DM.putIataInRow(row_idx=index, IATACode=FS.getIATACode(row["city"]))
DM.saveDataFrame()