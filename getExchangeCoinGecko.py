#!/usr/bin/python3
import json
import requests
import pandas as pd
from datetime import datetime
import os

# The following function retrieves all the Exchanges names and ID's identified by CoinGecko
if __name__ == "__main__":
    def get_exchange_symbols_coingecko():
        base_url = "https://api.coingecko.com/api/v3/"
        print("({}) Geting all Exchanges from Coin Gecko".format(str(datetime.today().strftime("%H:%M:%S:%f"))))
        req = requests.get(base_url + "/exchanges/list")
        res = json.loads(req.text)
        df_exchange_symbols = pd.DataFrame.from_dict(res) 
        df_exchange_symbols.index.name = 'index'
        output_folder= os.path.join(os.path.dirname(os.path.realpath(__file__)),"Output")
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        try:
            df_exchange_symbols.to_csv(os.path.join(output_folder, 'AllExchanges_CoinGecko_{}.csv'.format(str(datetime.today().strftime('%Y%m%d'))) ))
        except:
            print("It was not possible to save/create the file")
        print("({}) End of get_exchange_symbols_coingecko".format(str(datetime.today().strftime("%H:%M:%S:%f"))))
        return df_exchange_symbols

df_exchange_symbols = get_exchange_symbols_coingecko()