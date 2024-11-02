import requests
import json
# Including the Alpha Vantage API key

with open('creds.json', 'r') as file:
    JsonFile = json.load(file)

APIkey = JsonFile['API_KEY']
print(APIkey)

