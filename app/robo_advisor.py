from datetime import time, date, datetime
from time import strftime, strptime
import pandas as pd
from pandas.core.tools.datetimes import to_datetime
import custom_functions as cf
import requests
import os
from dotenv import load_dotenv


print("Please wait while we get all active symbols for further processing")

load_dotenv() # go get env vars from the .env file

# read env variables
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

valid_symbols = cf.get_active_symbols(ALPHAVANTAGE_API_KEY)
selected_symbols = []
# TODO: ask for a user input
while True:
    symbol = input("Please enter the stock or cryptocurrency symbol or DONE: ") 
    symbol = symbol.upper()
    if symbol in valid_symbols:
        selected_symbols.append(symbol)
        print(selected_symbols)
    elif "DONE" == symbol:
        break
    else:
        print("You entered invalid symbol. Please try again!")
     

print(selected_symbols)

# user input for risk tolerance
if len(selected_symbols) > 0:
    risk_tolerance = input("Enter your risk tolarence: ")
else:
    print("You didn't enter any stock or cryptocurrency symbol. Exiting the program")
    exit

# For each symbol, get response from API
# .. Store in the CSV File under data directory
# .. Reference for time format - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
for s in selected_symbols:
    return_values = []
    return_values = cf.get_response_data(s, ALPHAVANTAGE_API_KEY)
    # last_refreshed = return_values[0]
    timeseries_df =  return_values[1]
    # last_refreshed_time = time.fromisoformat(last_refreshed)
    last_refreshed = strptime(return_values[0], f"%Y-%m-%d")
    # print(type(last_refreshed))
    # print(last_refreshed)
    
    cf.store_timeseries_csv(s, timeseries_df)
    
    close_price = float(timeseries_df.loc[return_values[0], "close"])
    high_price = cf.get_recent_high_price(timeseries_df)
    low_price=cf.get_recent_low_price(timeseries_df)
    
    #Calculation Requirements
    print("*********************************************************")
    print(f"Stock: {s}")
    print("Run at: " + datetime.now().strftime(f"%I:%M %p on %B %dth, %Y"))
    print("Last Data from:", datetime(last_refreshed.tm_year, last_refreshed.tm_mon, last_refreshed.tm_mday).strftime(f"%B %dth, %Y"))
    print("Close price:", cf.to_usd(close_price))
    print("Recent high price:", cf.to_usd(high_price))
    print("Recent low price:", cf.to_usd(low_price))
    
    
    # Buy or Not to Buy
    if (close_price < low_price*(1+0.2)):
        print(f"""Our analysis recommends you should BUY this stock: {s}. Because the closing price is less than the set threshold (20% above the recent low price).""")

    else:
        print(f"""Our analysis recommends you should NOT BUY this stock: {s}. Because the closing price is greater than the set threshold (20% above the recent low price).""")

    print("*********************************************************")


    # Plots - close and low price trend over time. 
    # .. These graphs are opened in the browser new tab for each symbol
    cf.draw_trend_line(timeseries_df,s)