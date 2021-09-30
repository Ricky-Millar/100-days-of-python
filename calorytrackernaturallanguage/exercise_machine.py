import requests
class Exercise:

    def __init__(self, gender: str, weight_kg: str, height_cm: str, age: str, headers : dict):
        self.EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
        self.person_deets = {
            'gender': gender,
            'weight_kg': weight_kg,
            'height_cm': height_cm,
            'age': age,

        }
        self.headers = headers

    def query(self):
        query = input('what did you bench today?')
        self.person_deets['query']=query
        print(self.person_deets)
        self.answer = requests.post(url = self.EXERCISE_ENDPOINT, json = self.person_deets, headers= self.headers)
        print(self.answer.text)


