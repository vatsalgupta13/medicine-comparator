import requests
import json
BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE+"saltinformation/Acarbose")
print(response.json())

# resp = response.json()
# data = json.loads(resp)
# alternatives = data['list']
# temp = alternatives.split(',')
# print("Name of Salt : ", data['name'])
# print("Description : ", data['description'])
# print("Alternatives :")
# for i, j in enumerate(temp):
#     print(i+1, " ", j)
