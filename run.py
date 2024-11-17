import json
import yfinance as yf
import os
from getch import getch
import requests

GITHUB_TOKEN = os.getenv('CREDS_GITHUB')
if not GITHUB_TOKEN:
    with open('creds_API.json', 'r') as f:
        GITHUB_TOKEN = json.load(f)['key']
GIST_ID = "b060f951d0cadccba1b601a9ea219f67"

def clear_terminal():
    """
    Clear the terminal screen based on the operating system,
    For Windows, run the 'cls' command,
    For Mac and Linux, run the 'clear' command,
    """
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

def get_stock_price(symbol):
    """  
    Retrieve the latest closing stock price for a given symbol,
    - Create a Ticker object for the given stock symbol using yfinance,
    - Retrieve the historical price data for the stock for a 1-day period,
    - Access the closing price for the most recent day available,
    - The closing stock price as a float or numeric value.
    """
    stock = yf.Ticker(symbol)
    stock_price = stock.history(period="1d")['Close'].iloc[0]
    return stock_price
   
def get_symbol_list():
    """ 
    Retrieve a list of stock symbols from a local file,
    - Open the file 'stock_list.txt' in read mode,
    - Load the contents of the file as JSON data and store it in symbol_list,
    - The list of stock symbols.
    """
    with open('stock_list.txt', 'r') as file:
        symbol_list = json.load(file)
    return symbol_list

def load_creds():
    url = f"https://api.github.com/gists/{GIST_ID}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_file_url = response.json()["files"]["creds.json"]["raw_url"]
        creds = requests.get(json_file_url).json()
    else:
        print("Failed to fetch Gist:", response.status_code)
    return creds

def save_creds(creds):
    """
    Save updated credentials to the environment variable,
    Converts the dictionary to JSON and updates the CREDS_JSON environment variable,
    Gist API URL,
    Gist update payload,
    Authorization header,
    Send PATCH request to update the Gist.
    """
    creds_json = json.dumps(creds)
    url = f"https://api.github.com/gists/{GIST_ID}"
    payload = {
        "files": {
            "creds.json": {
                "content": creds_json
            }
        }
    }
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.patch(url, headers=headers, json=payload)

def assign_id():
    """
    Assigns a unique ID to a new user by scanning existing user data from a file,
    Attempts to load existing user data from the file `creds.json`,
       - If the file doesn't exist or contains invalid JSON, initializes an empty list.
    Iterates over the list of users to find the highest existing ID,
       - Assumes that each user in the list has an "id" field containing a numeric value.
    Increments the highest ID by one and returns it as the new unique ID,
    The next available numeric ID (highest ID in the data incremented by 1).
    """ 
    data = load_creds()   
    id_assigned = 0
    for user in data:
        id_assigned = int(user["id"])         
    id_assigned += 1
    return id_assigned

def load_portfolio(pin, password):
    """
    Loads a user's portfolio from the existing data file based on the provided PIN and password,
    Attempts to load user data from the file `creds.json`:
       - If the file does not exist or contains invalid JSON, initializes an empty list (`data`).
    Iterates through the list of user dictionaries to find a match for the provided PIN and password,
       - If a match is found:
         - Initializes a `Portfolio` object with the user's information.
         - Sets the portfolio attributes (`stock`, `investment`, `account_value`, and `buying_power`)
           based on the matched user data.
         - Calls the `save_update` method on the `Portfolio` object to save or update its data.
         - Prints a success message and returns `True` along with the `Portfolio` object.
       - If no match is found:
         - Prints an error message indicating that the user ID or password is incorrect.
         - Returns `False` and an empty list.
    """
    data = load_creds() 
    for user in data:
        if user["id"] == pin and user["password"] == password:
            my_portfolio = Portfolio(1000, password, pin)
            my_portfolio.stock = user["stock"]
            my_portfolio.investment = user["investment"]
            my_portfolio.account_value = user["account_value"]
            my_portfolio.buying_power = user["buying_power"]
            my_portfolio.save_update()
            print("Your account login was successful!!")
            return True, my_portfolio            
    print("User id or password does not match!!")
    return False, []


class Portfolio:
    def __init__(self, investment=0, password='none', number=-1, creds='creds.json'):
        """
        Initializes a Portfolio object with a given investment amount 
        """ 
        self.stock = {}
        self.investment = investment
        self.account_value = investment
        self.buying_power = investment
        self.password = password
        self.id = number
        self.creds = creds
        """
        Save or update user info in the creds.json file
        """
        self.save_update()


    def save_update(self):
        """
        Saves the current user's data to the file or updates it if the user already exists,
        Loads existing user data from the file specified in `self.creds`:
       - If the file does not exist or contains invalid JSON, initializes an empty list (`data`).
        Searches for the user in the loaded data by comparing their unique identifier (`self.id`):
       - If a match is found:
         - Updates the existing user's data with the current instance attributes,
       - If no match is found:
         - Appends a new dictionary containing the current user's data to the list,
        Writes the updated list of user data back to the file:
       - Saves the data in a human-readable JSON format with an indentation of 4 spaces.
        """
        data = load_creds()
        user_found = False
        for user in data:
            if user["id"] == self.id:
                user["stock"] = self.stock
                user["investment"] = self.investment
                user["account_value"] = self.account_value
                user["buying_power"] = self.buying_power
                user["password"] = self.password
                user_found = True
                break
        if not user_found:
            data.append({
                "stock": self.stock,
                "investment": self.investment,
                "account_value": self.account_value,
                "buying_power": self.buying_power,
                "password": self.password,
                "id": self.id,
                "creds": self.creds
            })
        save_creds(data)


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
            print(f"You have successfully added {number} {symbol} to your portfolio.")
            self.save_update()
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
                print(f"You have successfully sold {number} {symbol} from your portfolio.")
                self.save_update()
            else: 
                print(f"You do not have enough number of '{symbol}' stocks to sell")
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
        """ 
        Increases the portfolio's total investment and buying power by a specified amount. 
        """ 
        self.investment += amount
        self.buying_power += amount 
        print(f"You have successfully added {amount} to your account.")
        self.save_update()
    

    def withdraw(self, amount):
        """
        Verifies that the portfolio has sufficient buying power to process the withdrawal,
        If not, displays an error message.
        """
        if self.buying_power >= amount:
            self.investment -= amount
            self.buying_power -= amount 
            print(f"You have successfully withdrawn {amount} from your account.")
            self.save_update()
        else:
            print("You do not have enough liquidity!")


    def print_status(self):
        """ 
        Prints the current status of the portfolio, including buying power, account value, total investment, and stock holdings. 
        """
        self.update_account_value()
        print(f"Your buying power is: {self.buying_power}, your account value is {self.account_value}, your investment is {self.investment}, and the stocks in your portfolio are {self.stock}")


def main():
    """ 
    Run all program functions 
    """

    initial_selection = -1
    print("Welcome to Hawraa's Trading Platform.\n1 - Login an existing account\n2 - Create a new account\n0 - Quit")
    try:
        initial_selection = int(input("Please choose one of the three options above: \n"))
        flag_selection = True
        match initial_selection:
            case 1:
                id_number = int(input("Please enter your account id number: \n"))
                password = input("Please enter your account's password: \n")
                flag_selection, my_portfolio = load_portfolio(id_number, password)
            case 2:
                initial_investment = float(input("Please enter the amount you want to invest in your portfolio: \n"))
                password = input("Please enter a password for your account: \n")
                my_portfolio = Portfolio(initial_investment, password, assign_id())
                print(f"Congratulations!! You have successfully created your portfolio!!")
                print(f"Your id on the platform is {my_portfolio.id}. Please save it in a safe place together with your password!!")
            case 0: 
                flag_selection = False
                print("Thanks for using our platform!")
            case _:
                flag_selection = False
                print("Selection is invalid!!")

    except:
        flag_selection = False
        print("Error!! Selection is invalid!!")


    if flag_selection:
        selection = 100
        symbol_list = get_symbol_list()
        while selection > 0:
            print("Press any key to continue...")
            getch()
            clear_terminal()
            my_portfolio.print_status()
            print("Which operation would you like to do? Please choose an option by entering the corresponding number:\n1 - Buy a stock\n2 - Sell a stock\n3 - Increase your investment\n4 - Withdraw from your account\n0 - Quit")
            selection = int(input("\n"))
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
                case 0:
                    print("Thanks for using our platform!")
                case _:
                    print("Please select 1, 2, 3, 4, or 0")
            
main()