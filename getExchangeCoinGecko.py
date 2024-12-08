#!/usr/bin/python

import json
import requests
import pandas as pd
from datetime import datetime
import os
import logging
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

# Load configuration
CONFIG_FILE = "config.json"
DEFAULT_OUTPUT_FOLDER = "Output"

def load_config():
    """Load configuration settings from a JSON file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config_file:
            return json.load(config_file)
    else:
        logging.warning("Configuration file not found. Using defaults.")
        return {"base_url": "https://api.coingecko.com/api/v3/"}

# Get the current timestamp
def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')

# Get the current date in YYYYMMDD format
def current_date():
    return datetime.now().strftime('%Y%m%d')

# Retry mechanism for API requests
def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504)):
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

def get_exchange_symbols_coingecko(output_folder=DEFAULT_OUTPUT_FOLDER, export_to_file=True):
    """
    Retrieves exchange symbols from the CoinGecko API, saves the result to a CSV file, 
    and returns a pandas DataFrame.

    Args:
        output_folder (str): Path to save the output CSV file. Defaults to "Output".
        export_to_file (bool): Whether to save the data to a file. Defaults to True.

    Returns:
        pd.DataFrame: DataFrame containing the exchange data.
    """
    config = load_config()
    base_url = config.get("base_url", "https://api.coingecko.com/api/v3/")
    logging.info("Fetching all exchanges from CoinGecko.")

    try:
        session = requests_retry_session()
        response = session.get(base_url + "exchanges/list")
        response.raise_for_status()
        exchange_data = response.json()

        # Validate response
        if not isinstance(exchange_data, list):
            logging.error("Unexpected response format from API.")
            return None

        # Convert JSON data to DataFrame
        df_exchange_symbols = pd.DataFrame(exchange_data)
        df_exchange_symbols.index.name = "index"

        # Ensure output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            logging.info(f"Created output folder: {output_folder}")

        # Export to CSV
        if export_to_file:
            csv_filename = f"AllExchanges_CoinGecko_{current_date()}.csv"
            csv_filepath = os.path.join(output_folder, csv_filename)
            df_exchange_symbols.to_csv(csv_filepath, index=False)
            logging.info(f"Data saved to CSV: {csv_filepath}")

        logging.info(f"Retrieved {df_exchange_symbols.shape[0]} exchanges.")
        return df_exchange_symbols

    except requests.RequestException as e:
        logging.error(f"Error fetching data from CoinGecko: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

# Progress bar for data processing (future use)
def process_data_with_progress_bar(data, process_function):
    """
    Process a dataset with a progress bar.

    Args:
        data (iterable): The dataset to process.
        process_function (callable): The function to apply to each item.
    """
    for item in tqdm(data, desc="Processing data"):
        process_function(item)

if __name__ == "__main__":
    # Call the main function to fetch and process exchange symbols
    df_exchange_symbols = get_exchange_symbols_coingecko()
