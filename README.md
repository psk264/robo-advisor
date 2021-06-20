# robo-advisor
Project Assignment  - Robo Advisor 🤖 💰 🤓

# Objective
This repository holds the code for the robo-advisor project.  It helps user to enter their desired stock or cryptocurrency symbol and the program makes recommendation whether to buy or not buy the stock based on the following algorithm:

If the close price of the stock is less than 20% above the recent low price than buy.  Otherwise, do not buy. 

This program also shows two graphs which are automatically opened in the browser during program execution:
1. The close price and low price trend lines for the available timespan for the given stock or cryptocurrency symbol
2. The trend of percentage difference between close price and the recent low price for the given stock or cryptocurrency symbol (The program uses this % difference as threshold to assess whether the use should buy/not buy the stock)    

# Pre-requisite 
* Anaconda 3.7+
* Python 3.7+
* Pip
* Git Bash
* [Alphavantage API](https://www.alphavantage.co/documentation/)
* Browser (to view graphs)

# Packages
* [requests](https://pypi.org/project/requests/)
* [python-dotenv](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/dotenv.md)
* [pandas](https://pandas.pydata.org/docs/reference/index.html)
* [clipboard](https://pypi.org/project/clipboard/)
* [plotly.express](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/plotly.md)

# Setup
1. In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify following information:
```ALPHAVANTAGE_API_KEY="<key>"```
3. Add `.env` in the .gitignore file so this .env file is ignored by the version control to ensure user privacy
# Instructions

# Additional Information
* The code is arranged such that each module of code is written as a custom function.  All custom functions are stored in the ```custom_functions.py```.  The main code to run the program is in ```robo_advisor.py```
* This code also shows 
