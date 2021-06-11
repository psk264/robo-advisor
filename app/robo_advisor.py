import requests
import os
from dotenv import load_dotenv

load_dotenv() # go get env vars from the .env file

# read env variables
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

# TODO: ask for a user input
symbol = "MSFT"


request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

# make a request
response = requests.get(request_url)
print(type(response))
print(response.text)

