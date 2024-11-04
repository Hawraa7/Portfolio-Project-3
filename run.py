import requests
import json
""" Including the Alpha Vantage API key """

with open('creds.json', 'r') as file:
    JsonFile = json.load(file)
APIkey = JsonFile['API_KEY']

def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={APIkey}"
    response = requests.get(url)
    stock_data = response.json()
    stock_price = float(stock_data["Global Quote"]["05. price"])
    return stock_price

class Portfolio:
    def __init__(self, investment):
        self.stock = {}
        self.investment = investment
        self.account_value = investment
        self.buying_power = investment
    
    def buy_stock(self, symbol, number):
        stock_price = get_stock_price(symbol)
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
                stock_price = get_stock_price(symbol)
                overall_price = stock_price * number
                self.buying_power += overall_price
                self.stock[symbol] -= number
            else: 
                print(f"You do not have enough number of {symbol} stocks to sell")


        else:
            print(f"self.stock is not in the portfolio.")
        
    def update_account_value(self):
        account_value = self.buying_power
        for stock in self.stock:
            stock_price = get_stock_price(stock)
            account_value += stock_price * self.stock[stock]

    def increase_investment(self, amount):
        self.investment += amount
        self.buying_power += amount 
    
    def withdraw(self, amount):
        if self.buying_power >= amount:
            self.investment -= amount
            self.buying_power -= amount 
        else:
            print(f"you do not have enough liquidity!")

    def print_status(self):
        self.update_account_value()
        print(f"The buying power is: {self.buying_power}, the account value is {self.account_value}, the investment is {self.investment}, and the stocks are {self.stock}")







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
my_portfolio.buy_stock("AAPL", 10)
my_portfolio.print_status()