import requests
import json
url = "https://aves.ninjas.cl/api/birds"

# payload = {}
# headers = {}
# response = requests.request("GET", url, headers=headers, data=payload)
response = requests.get(url)
result = json.loads(response.text)
# print(type(response.text))
# print(type(result))

# print(result)
# print([post['name'] for post in result]) #me muestra todos los nombres de la lista

def request_json(url):
    return json.loads(requests.get(url).text)
