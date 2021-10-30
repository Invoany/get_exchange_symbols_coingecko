# How to get All Exchanges symbols by using Web Scraping
The following **Python** Script is a **simple** Script.

The main goal of the script is to retrieve information about **all the crypto exchanges** identified by *https://www.coingecko.com/en*

We are acessing the Website by using the Requests Library 
> import requests

Define the *base_url*
> base_url = "https://api.coingecko.com/api/v3/"

An then using *requests* to acess the information from get and saveit in a variable.
> req = requests.get(base_url + "/exchanges/list")

Because the information that we are getting is a **JSON** file, i.e., **dictionaires**, several **keys** and respective **values** we need to transform this data into a **dataframe** so we can work it later.
> req = requests.get(base_url + "/exchanges/list")
> res = json.loads(req.text)
> df_exchange_symbols = pd.DataFrame.from_dict(res) 

Let's not forget to give a proper name to our **index column**, in this case we can just keep it simple and name it *index* so it wont be **empty**
> df_exchange_symbols.index.name = 'index'

And finnaly just save the file to any location at your **choice!**
> df_exchange_symbols.to_csv('Output\AllExchanges_CoinGecko_{}.csv'.format(str(datetime.today().strftime('%Y%m%d'))))

This **method** is a little bigger because we are adding the **current date** to the file name!

We are also returning an **Dataframe** that contains this information.
