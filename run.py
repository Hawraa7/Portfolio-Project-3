import requests
import json
import csv
""" Including the Alpha Vantage API key """

with open('creds.json', 'r') as file:
    JsonFile = json.load(file)
APIkey = JsonFile['API_KEY']

def get_stock_price(symbol):
    """  
    Retrieves the current stock price for a given symbol using the Alpha Vantage API,
    Uses the "GLOBAL_QUOTE" function to obtain real-time quote data,
    Parses the JSON response and extracts the stock price, converting it to a float for accuracy.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={APIkey}"
    response = requests.get(url)
    stock_data = response.json()
    stock_price = float(stock_data["Global Quote"]["05. price"])
    return stock_price

def get_symbol_list():
    """ 
    Retrieves a list of stock symbols for all US-listed companies from the Alpha Vantage API,
    Reads the response content as CSV data and extracts each stock symbol,
    Skips the header row in the CSV data to start the list from the first symbol.
    """
    url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={APIkey}"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8').splitlines()
        csv_content = csv.reader(content)
        symbol_list = [row[0] for idx, row in enumerate(csv_content) if idx > 0]  
    else:
        print(f"Cannot retrieve the data: {response.status_code}")
    return symbol_list

class Portfolio:
    def __init__(self, investment):
        """ Initializes a Portfolio object with a given investment amount """
        self.stock = {}
        self.investment = investment
        self.account_value = investment
        self.buying_power = investment
    
    def buy_stock(self, symbol, number):
        """ 
        Purchases a specified number of shares of a given stock symbol if enough buying power is available,
        Retrieves the current stock price using the get_stock_price function,
        Calculates the total cost for purchasing the shares and checks if buying power is sufficient,
        If sufficient, updates the stock holdings and reduces the buying power by the total cost.
        """
        stock_price = get_stock_price(symbol)
        overall_price = stock_price * number
        if self.buying_power >= overall_price:
            if symbol in self.stock.keys():
                self.stock[symbol] += number
            else:
                self.stock[symbol] = number
            self.buying_power -= overall_price
        else:
            print("You do not have enough buying power!") 
    
    def sell_stock(self, symbol, number):
        """ 
        Checks if the specified stock symbol is in the portfolio,
        Ensures that there are enough shares available to sell; if not, displays an error message,
        Fetches the current stock price using the get_stock_price function,
        Calculates the total amount received from selling the specified number of shares and updates the buying power.
        """
        if symbol in self.stock:
            if self.stock[symbol] >= number:
                stock_price = get_stock_price(symbol)
                overall_price = stock_price * number
                self.buying_power += overall_price
                self.stock[symbol] -= number
            else: 
                print(f"You do not have enough number of {symbol} stocks to sell")
        else:
            print(f"The stock symbol '{symbol}' is not in the portfolio.")
        
    def update_account_value(self):
        """ 
        Updates the account value by recalculating it based on the current buying power 
        and the market value of all stocks held in the portfolio.
        """
        self.account_value = self.buying_power
        for stock in self.stock:
            stock_price = get_stock_price(stock)
            self.account_value += stock_price * self.stock[stock]

    def increase_investment(self, amount):
        """ Increases the portfolio's total investment and buying power by a specified amount."""
        self.investment += amount
        self.buying_power += amount 
    
    def withdraw(self, amount):
        """
        Verifies that the portfolio has sufficient buying power to process the withdrawal,
        If not, displays an error message.
        """
        if self.buying_power >= amount:
            self.investment -= amount
            self.buying_power -= amount 
        else:
            print("You do not have enough liquidity!")

    def print_status(self):
        """
        Prints the current status of the portfolio, including buying power, account value, total investment, and stock holdings.
        """
        self.update_account_value()
        print(f"The buying power is: {self.buying_power}, the account value is {self.account_value}, the investment is {self.investment}, and the stocks are {self.stock}")

def main():
    """ Run all program functions """ 
    selection = 100
    initial_investment = float(input("Welcome to Hawraa Trading Platform. Enter the amount you want to invest in your portfolio: \n"))
    my_portfolio = Portfolio(initial_investment)
    while selection > 0:
        symbol_list = get_symbol_list()
        selection = int(input("Please select 1 to buy a stock, 2 to sell a stock, 3 to increase your investment, 4 to withdraw from your account, 5 to check your account status or 0 to quit: \n"))
        match selection:
            case 1:
                symbol = input("Enter the stock name: \n")
                if symbol in symbol_list:
                    number = input(f"Enter the number of stock {symbol} you want to buy: \n")
                    try:
                        number = float(number)
                        if number > 0:
                            my_portfolio.buy_stock(symbol, number)
                        else:
                            print("The number you entered needs to be greater than zero!")
                    except:
                        print("The value you entered is invalid!")
                else:
                    print("The symbol you entered is invalid!")
            case 2:
                symbol = input("Enter the stock name: \n")
                if symbol in symbol_list:
                    number = input(f"Enter the number of stock {symbol} you want to sell: \n")
                    try:
                        number = float(number)
                        if number > 0:
                            my_portfolio.sell_stock(symbol, number)
                        else: 
                            print("The number you entered needs to be greater than zero!")
                    except:
                        print("The value you entered is invalid!")
                else:
                    print("The symbol you entered is invalid!")
            case 3:
                number = input("How much you want to increase your investment? \n")
                try:
                    number = float(number)
                    if number > 0:
                        my_portfolio.increase_investment(number)
                    else: 
                        print("The number you entered needs to be greater than zero!")
                except:
                    print("The value you entered is invalid!")
            case 4:
                number = input("Enter the number you want to withdraw from your account: \n")
                try:
                    number = float(number)
                    if number > 0:
                        my_portfolio.withdraw(number)
                    else:
                        print("The number you entered needs to be greater than zero!")
                except:
                    print("The value you entered is invalid!")
            case 5:
                my_portfolio.print_status()
            case 0:
                print("Thanks!")
            case _:
                print("Please select 1, 2, 3, 4, 5, or 0")
            
                

main()
            




