import requests
import json
""" Including the Alpha Vantage API key """

with open('creds.json', 'r') as file:
    JsonFile = json.load(file)
APIkey = JsonFile['API_KEY']

class Portfolio:
    def __init__(self, investment):
        self.stock = {}
        self.investment = investment
        self.account_value = investment
        self.buying_power = investment
    
    def buy_stock(self, symbol, number):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={APIkey}"
        response = requests.get(url)
        stock_data = response.json()
        stock_price = float(stock_data["Global Quote"]["05. price"])
        overall_price = stock_price * number
        if self.buying_power >= overall_price:
            if symbol in self.stock.keys():
                self.stock[symbol] += number
            else:
                self.stock[symbol] = number
            self.buying_power -= overall_price
        else:
            print(f"You do not have enough buying power") 
    
    
    def sell_stock(self, symbol, number):
        if (symbol in self.stock):
            if self.stock[symbol] >= number:
                url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={APIkey}"
                response = requests.get(url)
                stock_data = response.json()
                overall_price = stock_price * number
                self.buying_power += overall_price
                self.stock[symbol] -= number
            else: 
                print(f"You do not have enough number of {symbol} stocks to sell")


        else:
            print(f"self.stock is not in the portfolio.")
        
        




""" 
symbol = "AAPL"
#url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={APIkey}"
url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={APIkey}"
response = requests.get(url)
stock_data = response.json()
#print(stock_data['Time Series (Daily)']['2024-11-01']['2. high'])
print(stock_data["Global Quote"]["05. price"])

symbol = "ABBV"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={APIkey}"
response = requests.get(url)
stock_data = response.json()
"""
my_portfolio = Portfolio(1000)
my_portfolio.buy_stock("AAPL", 1)
print(f"The buying power is: {my_portfolio.buying_power}, the account value is {my_portfolio.account_value}, the investment is {my_portfolio.investment}, and the stocks are {my_portfolio.stock}")