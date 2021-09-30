import csv
# temp_list = []
# with open('weather_data.csv') as file:
#    data = csv.reader(file)
#    for row in data:
#        print(row)
#        if row[1].isnumeric():
#            temp_list.append(int(row[1]))
#
# print(temp_list)
#
import pandas

data = pandas.read_csv('weather_data.csv')
print(data)
print(data['temp'])

temp_list = data['temp'].to_list()
print(temp_list)
mean_temp = sum(temp_list)/len(temp_list)
print(mean_temp)
# TODO:or just do this
print(data['temp'].mean())
print(data['temp'].max())
# TODO:pandas actuly makes methods out of each columb to make calling them easier, CASE SENSITIVE
print(data.temp)
# TODO: ROWS, they are more complex
# TODO: the [] filters a column for something in perticular, in the table data, look for where the day is monday
print(data[data.day == 'Monday'])
# TODO:from indisde to outside:: this takes the max temp value, then finds the row that it is true, then finds that row in the table.
print(data[data.temp == data.temp.max()])
# TODO: find stuff within a row
monday = data[data.day == 'Monday']
#TODO: even when the variable has been saved by itself it retains info of where it is in the table.
print(monday.condition)
#TODO convert monday temp from C to F
Fahrenheit = (float(monday.temp) * 9/5) + 32
print(Fahrenheit)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data = data['Primary Fur Color']

print(data.value_counts())
data.value_counts().to_csv('bananarama')