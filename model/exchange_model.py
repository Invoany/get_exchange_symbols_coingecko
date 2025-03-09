import requests
import pandas as pd
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from model.data_treatment import load_config

def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504)):
    session = requests.Session()
    retry = Retry(total=retries, read=retries, connect=retries, backoff_factor=backoff_factor, status_forcelist=status_forcelist)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    return session

def get_exchange_symbols():
    config = load_config()
    base_url = config["base_url"]
    logging.info("Fetching exchanges from CoinGecko.")
    try:
        session = requests_retry_session()
        response = session.get(base_url + "exchanges/list")
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data) if isinstance(data, list) else None
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None