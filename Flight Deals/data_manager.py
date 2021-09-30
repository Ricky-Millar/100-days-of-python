import requests
class DataManager:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        pass

    def get_sheet_data(self):
        self.data = requests.get(url=self.endpoint)
        return self.data.json()

    def new_user(self, firstname,lastname,email):

        self.user_deets = {'user':{
            'firstname': firstname,
            'lastname' : lastname,
            'email' : email,}
        }
        response = requests.post(url='https://api.sheety.co/5b1e332caa8c97f81eb2d0f576cdf4d9/flightDeals/user', json = self.user_deets)
        print(response.text)

