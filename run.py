import requests
import json
import csv
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

def get_symbol_list():
    url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={APIkey}"
    response = requests.get(url)
    if response.status_code == 200:
        # read the content of the response as CSV
        content = response.content.decode('utf-8').splitlines()
        csv_content = csv.reader(content)
        
        # extract the symbols
        symbol_list = [row[0] for idx, row in enumerate(csv_content) if idx > 0]  # row[0] is the symbol
        #print("The symbols are: ", symbol_list)
    else:
        print("Cannot retrieve the data: ", response.status_code)
    
    return symbol_list

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
        self.account_value = self.buying_power
        for stock in self.stock:
            stock_price = get_stock_price(stock)
            self.account_value += stock_price * self.stock[stock]

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



def main():
    selection = 100
    initial_investment = float(input("Welcome to Hawraa Trading Platform. Enter the amount you want to invest in your portfolio: "))
    my_portfolio = Portfolio(initial_investment)
    while selection > 0:
        selection = int(input(f"Please select 1 to buy a stock, 2 to sell a stock, 3 to increase your investment, 4 to withdraw from your account, 5 to check your account status or 0 to quit: "))
        match selection:
            case 1:
                symbol = input("Enter the stock name: ")
                symbol_list = get_symbol_list()
                if symbol in symbol_list:
                    number = float(input(f"Enter the number of stock {symbol} you want to buy: "))
                    if number > 0:
                        my_portfolio.buy_stock(symbol, number)
                    else:
                        print(f"The number you entered is invalid!")
                else:
                    print(f"The symbol you entered is invalid!")
            case 2:
                symbol = input("Enter the stock name: ")
                number = float(input(f"Enter the number of stock {symbol} you want to sell: "))
                my_portfolio.sell_stock(symbol, number)
            case 3:
                number = float(input(f"How much you want to increase your investment? "))
                my_portfolio.increase_investment(number)
            case 4:
                number = float(input(f"Enter the number you want to  withdraw from your account: "))
                my_portfolio.withdraw(number)
            case 5:
                my_portfolio.print_status()
            case 0:
                print(f"Thanks!")
            case _:
                print(f"Please select 1, 2, 3, 4, 5, or 0")
            
                

main()
            




