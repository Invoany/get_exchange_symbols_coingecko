#!/usr/bin/python
import json
import requests
import pandas as pd
from datetime import datetime
import os

# The following function retrieves all the Exchanges names and ID's identified by CoinGecko

def current_timestamp():
    return str(datetime.today().strftime('%Y-%m-%d')) + " " + str(datetime.today().strftime("%H:%M:%S:%f"))

def current_date():
    return str(datetime.today().strftime('%Y%m%d'))

if __name__ == "__main__":
    def get_exchange_symbols_coingecko():
        base_url = "https://api.coingecko.com/api/v3/"
        print("({}) Geting all Exchanges from Coin Gecko".format(current_timestamp()))
        req = requests.get(base_url + "/exchanges/list")
        res = json.loads(req.text)
        df_exchange_symbols = pd.DataFrame.from_dict(res) 
        df_exchange_symbols.index.name = 'index'
        output_folder= os.path.join(os.path.dirname(os.path.realpath(__file__)),"Output")
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
            print("({}) output_folder was created".format(current_timestamp()))
        else:
            print("({}) output_folder already created".format(current_timestamp()))
        try:
            df_exchange_symbols.to_csv(os.path.join(output_folder, 'AllExchanges_CoinGecko_{}.csv'.format(current_date()) ))
            print("({0}) Dataframe exported to CSV as AllExchanges_CoinGecko_{1}.csv".format(current_timestamp(),current_date()))
        except:
            print("({}) It was not possible to save/create the file".format(current_timestamp()))
        print("({0}) There is a total of {1} lines".format(current_timestamp(),str(df_exchange_symbols.shape[0])))
        print("({}) End of get_exchange_symbols_coingecko".format(current_timestamp()))
        return df_exchange_symbols

df_exchange_symbols = get_exchange_symbols_coingecko()