# Hawraa's Trading Platform 
Hawraa's Trading Platform is a digital interface or software system that enables users to buy, sell, and manage financial assets such as stocks.

The platform is typically designed to facilitate a range of investment activities for individuals, financial advisors, or institutional investors.

In my project, which runs in the Code Institute mock terminal on Heroku, the platform enables users to interactively manage a stock portfolio, simulating trading activities like buying, selling, depositing, and withdrawing funds, all while maintaining an up-to-date portfolio value.

In this Project-Portfolio, the Platform offers tools to manage and track the investment, showing gains, losses, and asset allocation.

Here is the live version of my project.

![Screenshot of the live version of the project](Screenshotversion.png)

## How to start investing on the platform?

The base of the platform is a digital investment portfolio management system that allows users to manage stock holdings and cash investments interactively. The yfinance library is a powerful tool that allows the user to access stock market data for a variety of companies in real time, making it useful for tracking and trading stocks. 

Yfinance provides up-to-date information on stock prices. In this setup, the user use yfinance to get stock price data for buying and selling stocks in his portfolio.

First, the user choose one of 3 options: create a portfolio or log in his portfolio or quit the platform. When he choose the first option, he has an id number and password and the program check if the selection is valid. When he choose the second option, he create a portfolio and the program give him an id and password. Next, when the portfolio is create, the user has a liberty to enter an initial investment amount that will act as starting buying power. This is the cash available to make his first stock purchases and he start the investemnt by choosing the different option he has: buyin, selling the stocks, increasing or withdrawing the funds.

The platform offers more options for the user to choose what and how he wants to invest.

## Features

### Existing Features

- Initial Investment Setup:
  - The user starts by logging in his portfolio or creating one if he has not. 
  - Next, he enters an initial investment amount and a password in case he chose to create a new account.
  - Then, he has more options to invest in his portfolio.

![Screenshot of the investment](Screenshotinvestment.png)
- Option 1 : Buying Stocks

  - The user purchases stocks by specifying a stock symbol and the number of stocks he wants to buy.
  - The platform checks if the user has enough buying power to complete the purchase. If they do, it adds the stocks to the portfolio and deducts the cost from their buying power.
![Screenshot of buying stocks](Screenshotbuying.png)
- Option 2: Selling Stocks

  - The user can sell stocks he owns by specifying the symbol and quantity.
  - The platform checks if the user owns enough stocks to sell the requested amount. If so, it sells the shares, adds the sale proceeds to the buying power, and updates the stock quantity.
![Screenshot of selling stocks](Screenshotselling.png)
- Stock Symbol Verification

  - When buying or selling stocks, the platform checks if the entered stock symbol is valid by consulting a list of stock symbols from an external data source.

- Option 3: Increasing Investment

  - Users can increase the cash in their portfolio by adding more funds to their initial investment and available buying power. The condition to increase the investment is that the number needs to be greater than zero.
![Screenshot of increasing investment](Screenshotincreasing.png)
- Option 4: Withdrawing Funds

  - Users can withdraw money from their available buying power. The platform ensures that the user has enough funds to cover the withdrawal. Also here, the condition to withdraw funds is the positive value of the number which the user wants to withdraw.
![Screenshot of withdrawing funds](Screenshotwithdrawing.png)
- Account Status Check:

  - Users can check their portfolio's current status, which includes:
    - Buying Power: The cash available to buy or sell more stocks.
    - Account Value: The total value of the portfolio, including both cash and stocks (using current stock prices from the yfinance library).
    - Investment: The initial invested amount plus any additional funds added.
    - Stock Holdings: A list of the stocks in the portfolio, including symbols and quantities.
![Screenshot of the portfolio's status](Screenshotportfoliostatus.png)
### Future Features

- Allow users to collaborate on investments, share insights, and collectively analyze market trends.

- Allow users to test their algorithms against historical data to evaluate potential performance.

- Allow user to control over data storage using decentralized systems to enhance privacy and security.

## Portfolio Model

I decided to use the portfolio class as my model. This allows users to track their investment progress, make informed decisions, and adjust their investment strategy in real-time.

This model tracks each user’s portfolio, including total account value, buying power (cash available for investment), initial investment amount, and the number of owned stocks.

The platform has methods to help users to manage stock holdings and cash investments interactively, such as a print method, an input method, a clear_terminal method, a get_stock_price method, a get_symbol_list method, an assign_id method, a load_portfolio method, a save_update method, a buy_stock method, a sell_stock method, an update_account_value method, an increase_investment method, and finally a withdraw_funds method.

## Testing

I have manually tested this project by doing the following:

- Passed the code through a PEP8 Python Validator and confirmed there are no problems.

- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice.

- Tested in my local terminal and the Code Institute Heroku terminal.

### Bugs

#### Solved Bugs

- The program did not work initially when the input by a user was invalid and errors were returned regarding the inconsistent format. I solved the problem by handling the error using *if-else* conditioning and *try-except* approach to return error messages for the user in case of invalid entries.

- The user had to press the enter key when requested to push any key to continue. Now this is solved using the *getch* function instead of the *input* function.

- Getting the current stock price and the list of available stocks was done initially using the [Alpha Vantage](https://www.alphavantage.co/) API. However the access there is limited in the free edition to 25 requests per day which is quite restrictive since an error directly appears after 25 requests asking me to buy the premium edition for a quasi-continuous number of requests. I found then an alternative solution by using the yahoo finance API to get the current price of a stock. Although unlike the case when using the Alpha Vantage API, the price is not a real-time price since it has a delay of up to 15 minutes but it is free and sufficient to use in my Portfolio project. As for the list of current stocks symbols in the market I got them from wikipedia and saved them in the file *"stock_list.txt"*.

- The Heroku application crushed when I tried to use the Heroku's API in order to edit the creds.json file stored in it. And the performance was not reliable, so I had to switch to Github's API that allows the access and editing of the creds.json file stored as a Gist in my Github's account.

### Remaining Bugs

- No bugs remaining

### Validator Testing

- PEP8

  - No errors were returned from [PEP8online.com](https://pep8ci.herokuapp.com/)

  ## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment: 

   - Fork or clone this repository 
   - Create a new Heroku app
   - Set the buildbacks to *Python* and *NodeJS* in that order
   - Link the Heroku app to the repository
   - Create a *CREDS_GITHUB* variable that stores the API key to access the *creds.json* file stored as a Gist in the Github account hosting the project. This is essential in order to limit the access only to the administrator who is managing the accounts on *Hawraa's trading platform*.
   - Click on Deploy Branch

   ## Credits

- Code Institute for the deployment terminal
- Yahoo finance library (yfinance) for getting real-time prices of stocks
- Wikipedia for getting the list of symbols for all the stocks 












