import requests
from datetime import datetime
today = datetime.now()
date = today.strftime('%Y%m%d')
pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'rickymillar'
PASSWORD = 'qpwoeirutyalskdjfhg'
user_params = {
    'token':PASSWORD ,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes' ,
    'notMinor' : 'yes'
}
headers = {
    'X-USER-Token': PASSWORD
}
graph_config = {
    'id': 'graph1',
    'name':'juggling graph',
    'unit' : 'Balls',
    'type' : 'int',
    'color' : 'momiji'

}
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

post_config = {
    'date':date,
    'quantity':'3',
}
print(date)
graph1_post_endpoint = f'{graph_endpoint}/graph1'
#making a account
# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

#making a new graph
# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print (response.text)

#making a post on the graph
response = requests.post(url = graph1_post_endpoint, headers = headers, json = post_config)
print(response.text)

