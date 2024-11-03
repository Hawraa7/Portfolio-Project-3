import requests
import json
# Including the Alpha Vantage API key

with open('creds.json', 'r') as file:
    JsonFile = json.load(file)
APIkey = JsonFile['API_KEY']





symbol = "AAPL"
#url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={APIkey}"
url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={APIkey}"
response = requests.get(url)
stock_data = response.json()
#print(stock_data['Time Series (Daily)']['2024-11-01']['2. high'])
print(stock_data["Global Quote"]["05. price"])


