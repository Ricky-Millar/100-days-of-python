from exercise_machine import Exercise
from sheet_generator import Sheety
import os
#--------secret sauce -----------#
#TODO: make this more secret using environment variables
EXE_APP_ID = '22e7e5aa'
EXE_APP_KEY = '791499385274c0566a04971b76317cd4'
SHEETS_ENDPOINT = 'https://api.sheety.co/5b1e332caa8c97f81eb2d0f576cdf4d9/myWorkoutsPythonProject/workouts'
sheets_headers = {"Authorization": "Bearer REALLYSECRETTOKENOFMINE"}
EXE_headers = {
    'x-app-id' : EXE_APP_ID,
    'x-app-key': EXE_APP_KEY
}
#---------------initial config
EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
#TODO: make this something that can be input by the person then saved in a file to be loaded for future use
gender = 'male'
weight_kg = '75'
height_cm = '184'
age = '26'


#----------input exercise and get response
ricky = Exercise(gender, weight_kg, height_cm, age, EXE_headers)
ricky.query()

#---------send to google sheet

ricky_sheet = Sheety(sheets_end_point= SHEETS_ENDPOINT, headers= sheets_headers)
ricky_sheet.add_to_sheet(ricky)
