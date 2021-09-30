import requests
from datetime import datetime
from exercise_machine import Exercise
class Sheety:
    def __init__(self, sheets_end_point, headers):
        self.end_point = sheets_end_point
        self.headers = headers
        pass

    def add_to_sheet(self, exercise_machine: Exercise):
        #TODO Add exeption, this will only work if done in the right order
        self.answer = exercise_machine.answer.json()
        print(self.answer["exercises"])
        self.answer_list = self.answer["exercises"]

        now = datetime.now()
        date = f"{now.strftime('%d')}/{now.strftime('%m')}/{now.strftime('%Y')}"
        time = now.strftime('%X')
        for i in range(len(self.answer_list)):
            to_post = {
                "workout": {
                    'date': date,
                    "time": time,
                    "exercise": self.answer_list[i]["name"],
                    'duration': self.answer_list[i]['duration_min'],
                    'calories': self.answer_list[i]["nf_calories"],
                }
            }
            post_debug = requests.post(url = self.end_point, json = to_post, headers = self.headers)
            print(post_debug.text)
