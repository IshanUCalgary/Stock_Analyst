# Stock_Analyst

This is a stock analyzer.
The Stock Analyst scrapes the web for relevant information and statistics about a company in the NYSE. 
It reports basic information such as the P/E Ratio, Beta, 52-Week High/Low, Current Ratio, Book Value and the Company's profile, such as Industry, sector etc.

The Analyst also does an Intrinsic Value Analysis that scrapes the web to find the intrinsic value of a company and reports if the stock is overvalued, undervalued etc. Concepts learned from value investing.

It also computes the Capital Asset Pricing Model (CAPM) by calculating the market risk premium and scraping the web for risk free rate and the beta. 

The scraping is done using Selenium and Chrome Web-driver. 

Pre Requistes:
  Selenium
  Chrome Driver

To Run:
  python3 analyzeStock.py <stock_ticker>
  For example:
    python3 analyzeStock.py BRK-B

If you are using a Mac, allow chromedriver to run from thes System Preferences. 
