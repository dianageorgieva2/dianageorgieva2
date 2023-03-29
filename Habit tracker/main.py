import requests
from datetime import datetime
USERNAME = "dianageorgieva2"
TOKEN = "sdhcbsjd37dc"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"


user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPHID,
    "name": "Fitness graph",
    "unit": "day",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()

pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many fitness sessions did you had today?"),
    }

response = requests.post(url=pixel_creation, json=pixel_parameters, headers=headers)
print(response.text)

pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20230327"
update_parameters = {
    "quantity": "4",
    }

# response = requests.put(url=pixel_update, json=update_parameters, headers=headers)
# print(response.text)

# pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=pixel_delete, headers=headers)
# print(response.text)
