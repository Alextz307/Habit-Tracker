import requests
from datetime import datetime

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'alextz307'
TOKEN = 'nde34wniud7328329hweiudb43euiw3242deiuw'
GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
GRAPH_ID = 'graph1'
PIXEL_CREATION_ENDPOINT = f'{GRAPH_ENDPOINT}/{GRAPH_ID}'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(user_response.text)

graph_params = {
    'id': GRAPH_ID,
    'name': 'Coding',
    'unit': 'Hours',
    'type': 'float',
    'color': 'sora'
}

graph_headers = {
    'X-USER-TOKEN': TOKEN
}

# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=graph_headers)
# print(graph_response.text)

today = datetime.now()
formatted_date = today.strftime('%Y%m%d')

pixel_creation_params = {
    'date': formatted_date,
    'quantity': input('How many hours did you code today? ')
}

pixel_creation_headers = {
    'X-USER-TOKEN': TOKEN
}

# pixel_creation_response = requests.post(url=PIXEL_CREATION_ENDPOINT,
#                                         json=pixel_creation_params, headers=pixel_creation_headers)
# print(pixel_creation_response.text)

PIXEL_UPDATE_ENDPOINT = f'{PIXEL_CREATION_ENDPOINT}/{formatted_date}'

pixel_update_params = {
    'quantity': '10'
}

pixel_update_headers = {
    'X-USER-TOKEN': TOKEN
}

# pixel_update_response = requests.put(url=PIXEL_UPDATE_ENDPOINT,
#                                      json=pixel_update_params, headers=pixel_update_headers)
# print(pixel_update_response.text)

PIXEL_DELETE_ENDPOINT = f'{PIXEL_CREATION_ENDPOINT}/{formatted_date}'

pixel_delete_headers = {
    'X-USER-TOKEN': TOKEN
}

# pixel_delete_response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=pixel_delete_headers)
# print(pixel_delete_response.text)
