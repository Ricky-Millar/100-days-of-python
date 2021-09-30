from datetime import datetime , timedelta


class FlightData:
    def __init__(self, data_manager_object, flight_search_object):
        self.sheety_object = data_manager_object
        self.search_object = flight_search_object

        self.time_now = datetime.now()
        self.time_in_6_months = self.time_now + timedelta(days=180)

        print(self.time_now, self.time_in_6_months)
        self.time_now = f"{self.time_now.strftime('%d')}/{self.time_now.strftime('%m')}/{self.time_now.strftime('%Y')}"
        self.time_in_6_months = f"{self.time_in_6_months.strftime('%d')}/{self.time_in_6_months.strftime('%m')}/{self.time_in_6_months.strftime('%Y')}"

        self.json_frame = {
      "fly_to": "", # this input an take multiple inputs as part of a string seperated by commas
      "fly_from": "AKL,CHC",
      "date_from": self.time_now,
      "date_to": self.time_in_6_months,
      "nights_in_dst_from": 7,
      "nights_in_dst_to": 28,
      "flight_type": "round",
      "one_for_city": 1,
    "max_stopovers": 2,
    "curr": "NZD",
    "price_to" : 5000,
}

    # def flight_config(self):
    #     self.json_frame["fly_from"] =
    #     self.json_frame[]

    def format_and_search(self):
        self.num_of_flights = 0
        self.current_flights = {}
        self.raw_data = self.sheety_object.get_sheet_data()
        self.number_of_destinations = len(self.raw_data["prices"])
        for i in range(self.number_of_destinations): #itterates through the desired flights from the google sheets class, and sends them to the flight search to check for flights.
            iataCode = self.raw_data["prices"][i]["iataCode"]
            lowestPrice = self.raw_data["prices"][i]["lowestPrice"]
            self.json_frame["fly_to"] = iataCode
            self.json_frame["price_to"] = lowestPrice

            self.flight_data = self.search_object.search(json=self.json_frame)
            if self.flight_data != None:         #Takes all the found flights and combines them into a dictionary to be stored
                #print(self.flight_data)
                #print(self.flight_data['flyfrom'])
                self.current_flights[self.num_of_flights] = self.flight_data
                self.num_of_flights += 1        #This itterated seperatly form the for loop, as if there are no flights returned, the i number will increase anyway, this will only increase if a floght is found
        return self.current_flights



