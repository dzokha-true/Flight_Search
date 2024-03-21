class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data ):
        try:
            data["data"][0]
        except IndexError:
            print(f"No flights found for {self.destination_city}.")
            return None
        # self.return_date = data["data"][1]["local_departure"].split("T")[0]
        self.out_date = data["data"][0]["local_departure"].split("T")[0]
        self.destination_airport = data["data"][0]["flyTo"]
        self.destination_city = data["data"][0]["cityTo"]
        self.origin_airport = data["data"][0]["flyFrom"]
        self.origin_city = data["data"][0]["cityFrom"]
        self.price = data["data"][0]["price"]

    def decodeData(self):
        result = f"${self.price} to fly from {self.origin_city}-{self.origin_airport} to  {self.destination_city}--" \
                 f"{self.destination_airport}"
        return result

    def returnPrice(self):
        return self.price