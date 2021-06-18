from datetime import time
import pandas as pd
import clipboard
import requests
from requests.models import Response
import json
import os

# Function to get all the valid active symbol which will be used for user input validation
def get_active_symbols(API_KEY):
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    CSV_URL = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={API_KEY}'
    print("CSV REPONSE URL:", CSV_URL)

    with requests.Session() as s:
        response = s.get(CSV_URL)
        csv_file_content = response.content.decode('utf-8')
        if len(csv_file_content) > 0:
            clipboard.copy(csv_file_content)
            active_symbols_df = pd.read_clipboard(",")
            # print(active_symbols_df.head())
            return active_symbols_df["symbol"].to_list()
        else:
            return 0

# Function to process the response text from the TIME SERIES DAILY ADJUSTED API call
def get_response_data(symbol, API_KEY):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}"
    print("API URL:", request_url)
    
    # make a request
    response = requests.get(request_url)  #response is of type string 
    
    response_eval = eval(response.text) #eval changes str to dict
    last_refreshed = response_eval["Meta Data"]["3. Last Refreshed"]

    timeseries_dict = response_eval["Time Series (Daily)"]

    # print(response_eval)
    # print(len(timeseries_dict))
    # print(type(timeseries_dict))
    
    timeseries_df = pd.DataFrame.from_dict(timeseries_dict, orient='index')
    # print(type(timeseries_df))
    # print(timeseries_df)
    
    #clean up of column name
    # print(timeseries_df.columns)
    column_name_list = []
    for item in timeseries_df.columns:
        item = item.split(". ")[1]
        column_name_list.append(item)
    timeseries_df.columns = column_name_list
    
    #selected retain column data only
    timeseries_df.pop("adjusted close")
    timeseries_df.pop("dividend amount")
    timeseries_df.pop("split coefficient")
    return [last_refreshed, timeseries_df]
    


# Function to store the timeseries for the given symbol into CSV file
def store_timeseries_csv(symbol, timeseries_df):
    if(len(timeseries_df) > 0):
        # print(len(timeseries_df))
        dir_name = "data"
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            print("Directory", dir_name, " already exists!")

        filename = f"{dir_name}\\prices_{symbol}.csv"
        print("Storing the data in csv file:", filename)
        with open(filename, "w") as file:
            # Convert dataframe to csv format using https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
            
            # and write it in file 
            timeseries_df.to_csv(filename, index_label="timestamp")
    else:
        print("Sorry, data file cannot be save! No data found to store in file.")
        exit()

# Function to convert price in readable format.  Adopted from Professor Rossetti's repo used in class of Summer 2021
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


def get_recent_high_price(timeseries_df):
    #get first 100 rows
    top10_rows = timeseries_df.head(100)
    high_price_series = top10_rows['high']
    # print(type(high_price_series)) 
    index =  pd.to_numeric(high_price_series).idxmax()    
    high_price = timeseries_df.loc[index, ['high']]
    # print(high_price)
    return float(high_price[0])


def get_recent_low_price(timeseries_df):
    top10_rows = timeseries_df.head(100)
    low_price_series = top10_rows['low']
    # print(type(low_price_series)) 
    index =  pd.to_numeric(low_price_series).idxmin()    
    low_price = timeseries_df.loc[index, ['low']]
    return float(low_price[0])
