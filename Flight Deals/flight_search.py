import requests
class FlightSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.flight_data = []
        self.destination_data = {}


    def search(self, json):
        # print(json)
        got = requests.get(url='https://tequila-api.kiwi.com/v2/search',params = json, headers = self.api_key )
        # print (got.text)
        data = got.json()
        try:
            flyfrom = data["data"][0]["cityFrom"]
            flyto = data["data"][0]["cityTo"]
            price = data["data"][0]["conversion"]["NZD"]
            self.flight_data = {
                "flyfrom" : flyfrom,
                "flyto" : flyto,
                "price" : price,
            }
            return self.flight_data
        except:
            return

    # def generate_abriviations(self,sheety_object):
    #     self.sheety_object = sheety_object
    #     response = requests.get(url='https://api.sheety.co/5b1e332caa8c97f81eb2d0f576cdf4d9/flightDeals/prices')
    #     data = response.json()
    #     self.destination_data = data["prices"]
    #     print(self.destination_data)
    #
    #     if self.destination_data[2]["iataCode"] == "":
    #         for city in self.destination_data:
    #             new_data = {
    #                 "price": {
    #                     "iataCode": city["iataCode"]
    #                 }
    #             }
    #             response = requests.put(
    #                 url=f"{'https://api.sheety.co/5b1e332caa8c97f81eb2d0f576cdf4d9/flightDeals/prices'}/{city['id']}",
    #                 json=new_data
    #             )
    #             print(response.text)




