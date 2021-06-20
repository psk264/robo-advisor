# robo-advisor
Project Assignment  - Robo Advisor 🤖 💰 🤓

# Objective
This repository holds the code for the robo-advisor project.  It helps user to enter their desired stock or cryptocurrency symbol and the program makes recommendation whether to buy or not buy the stock based on the following algorithm:

If the close price of the stock is less than 20% above the recent low price than buy.  Otherwise, do not buy. 
<br> <img src="https://user-images.githubusercontent.com/84349071/122690084-62d12b00-d1f5-11eb-91ed-b95dac14b547.png" alt="command-line-output" width="600" height="400"> <br>

It stores the specified data in the csv file under /data directory: 
<br> <img src="https://user-images.githubusercontent.com/84349071/122690573-57cbca00-d1f8-11eb-9fb5-9ccb356cb915.png" alt="price-trend" width="600" height="400"> <br>

This program also shows two graphs which are automatically opened in the browser during program execution:
1. The close price and low price trend lines for the available timespan for the given stock or cryptocurrency symbol
<br> <img src="https://user-images.githubusercontent.com/84349071/122690131-b479b580-d1f5-11eb-933d-95976287865c.png" alt="price-trend" width="600" height="400"> <br>
2. The trend of percentage difference between close price and the recent low price for the given stock or cryptocurrency symbol (The program uses this *% difference* as threshold to assess whether the use should buy/not buy the stock)  
<br> <img src="https://user-images.githubusercontent.com/84349071/122690115-9dd35e80-d1f5-11eb-99c0-b35bfad7c1c7.png" alt="percent-diff-trend" width="600" height="400"> <br>
  
## Supported Features
1. User input: single or multiple stock or cryptocurrency symbol
2. Input validation: Validate the user input against the list of valid symbols pulled from API
3. Terminal output: **_shown in screenshot above_** <br> 
```Stock: MSFT
   Run at: 06:27 PM on June 20th, 2021
   Last Data from: June 18th, 2021
   Close price: $259.43
   Recent high price: $263.19
   Recent low price: $224.26
   Recommendation
``` 
4. Data for each stock symbol stores in the ```.csv``` file under ***data*** directory under root folder **_Shown in the screenshot above_** <br>
```timestamp,open,high,low,close,volume
2021-06-18,259.63,262.3,258.75,259.43,37202217
2021-06-17,256.065,261.75,256.01,260.9,27565537
```
5. Graphs: **_shown in screenshot above_**
6. Recommendation to buy/not buy  

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
1. Register and get your Alphavantage API key from website: https://www.alphavantage.co/support/#api-key
2. In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify following information:
```ALPHAVANTAGE_API_KEY="<key>"```
2. Add `.env` in the .gitignore file so this .env file is ignored by the version control to ensure user privacy 
3. In the root directory of your local repository, create a new file called "requirements.txt" and update it with the following packages:
```requests
   python-dotenv
   pandas
   clipboard
   # For plotting graphs
   plotly.express
```

# Instructions
1. Use git client to clone or download this remote repository, [robo-advisor](https://github.com/psk264/robo-advisor), on your local machine.  Note the location where it is cloned or downloaded
2. Use command line application to navigate to the location where this repository was cloned or downloaded.  Ensure that ``<base>`` from conda initialization is shown on cmd line.  If ``<base>`` is not shown then, before proceeding, run command:<br/>
```conda init bash```
3. Since this code uses specific packages like python-dotenv, it is recommended to create a new project specific anaconda virtual environment. Here we create virtual environment name "stocks-env" using following command.  To create a environment with a different name, simply replace rpc-game-env with desired name:<br/>
``` conda create -n stocks-env python=3.8```
4. Activate the Anaconda environment "stocks-env" using the command:<br/>
```conda activate stocks-env```
5. After virtual environment is active i.e. ``<stocks-env>`` is shown on command-line, then install the third-party package python-dotenv on this virtual environment using command:<br/>
 ```pip install -r requirements.txt```<br/>
**NOTE:** The requirements.txt file is already provided in the repository.  If needed, feel free to delete and create one with all the above mentioned packages from setup section 
6. After the setup is complete, start the program using one of the following commands:<br/>
```python app/robo-advisor.py```   
**Note**: The inital request to the Alphavantage API takes some time since it is pulling data on all valid symbols and storing it in the internal list variable.

# Additional Information
* The code is arranged such that each module of code is written as a custom function.  All custom functions are stored in the ```custom_functions.py```.  The main code to run the program is in ```robo_advisor.py```
