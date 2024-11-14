# Investment Trading PLatform 
Investment Tading Platform is a digital interface or software system that enables users to buy, sell, and manage various financial assets such as stocks, bonds, ETFs, options, cryptocurrencies, and other securities.

The platform are typically designed to facilitate a range of investment activities and trading strategies for individuals, financial advisors, or institutional investors.

In my project, which runs in the Code Institute mock terminal on Heroku, the platform enables users to interactively manage a stock portfolio, simulating trading activities like buying, selling, depositing, and withdrawing funds, all while maintaining an up-to-date portfolio value.

In this Project-Portfolio, the Platform offers tools to manage and track the investment, showing gains, losses, and asset allocation.

Here is the live version of my project.
(screenchot).......................

## How starting investing on the platform ?

The base of the platform is a digital investment portfolio management system that allows users to manage stock holdings and cash investments interactively. The yfinance library is a powerful tool that allows the user to access stock market data for a variety of companies in real time, making it useful for tracking and trading stocks. 

Yfinance provides up-to-date information on stock prices. In this setup, the user use yfinance to get stock price data for buying and selling stocks in his portfolio.

First, the user enters an initial investment amount that will act as starting buying power. This is the cash available to make his first stock purchases.

The platform offers more options for the user to choose what and how he wants to invest.

## Features

### Existing Features

- Initial Investment Setup:
  - The user starts by entering an initial investment amount to create his portfolio.
  - Next, he has more options to invest his amount.
(screenshot).....................
- Option 1 : Buying Stocks

  - The user purchases stocks by specifying a stock symbol and the number of stocks they want to buy.
  - The platform checks if the user has enough buying power to complete the purchase. If they do, it adds the stocks to the portfolio and deducts the cost from their buying power.
(screenshot)....................
- Option 2: Selling Stocks

  - The user can sell stocks they own by specifying the symbol and quantity.
  - The platform checks if the user owns enough stocks to sell the requested amount. If so, it sells the shares, adds the sale proceeds to the buying power, and updates the stock quantity.
(screenshot).....................
- Stock Symbol Verification

  - When buying or selling stocks, the platform checks if the entered stock symbol is valid by consulting a list of stock symbols from an external data source.

- Option 3: Increasing Investment

  - Users can increase the cash in their portfolio by adding more funds to their initial investment and available buying power. The condition of increase the investment is the number needs to be greater than zero.
(screenshot).....................
- Option 4: Withdrawing Funds

  - Users can withdraw money from their available buying power. The platform ensures that the user has enough funds to cover the withdrawal. Also here, The condition of withdraw funds is the positive value of the number which user wants to withdraw.
(screenshot).....................
- Account Status Check:

  - Users can check their portfolio's current status, which includes:
    - Buying Power: The cash available to buy or sell more stocks.
    - Account Value: The total value of the portfolio, including both cash and stocks (using current stock prices from the yfinance library).
    - Investment: The initial invested amount plus any additional funds added.
    - Stock Holdings: A list of the stocks in the portfolio, including symbols and quantities.
(screenshot lal check wl if wl else).....................
### Future Features

- Allow users to collaborate on investments, share insights, and collectively analyze market trends.

- Allow users to test their algorithms against historical data to evaluate potential performance.

- Allow user to control over data storage using decentralized systems to enhance privacy and security.

## Portfolio Model

I decided to use the portfolio class as my model. This centralized allowing users to track their investment progress, make informed decisions, and adjust their investment strategy in real-time.

This model tracks each user’s portfolio, including total account value, buying power (cash available for investment), and initial investment amount.

The platform has methods to help users to manage stock holdings and cash investments interactively, such as a ....print method to print ou the ..........., an ......input method to ........

## Testing

I have manually tested this project by doing the following:

- Passed the code through a PEP8 Python Validator and confirmed there are no problems.

- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice.

- Tested in my local terminal and the Code Institute Heroku terminal.

### Bugs

#### Solved Bugs

.....................

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
   - Set the buildbacks to Python...... and NodeJS......in that order
   - Link the Heroku app to the repository
   - click on Deploy Branch

   ## Credits

- Code Institute for the deployment terminal
- ............












