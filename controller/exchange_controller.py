from model.exchange_model import get_exchange_symbols
from model.data_treatment import current_date
import logging
import os

def save_exchange_data():
    df = get_exchange_symbols()
    if df is not None and not df.empty:
        output_folder = "Output"
        os.makedirs(output_folder, exist_ok=True)
        file_path = os.path.join(output_folder, f"AllExchanges_{current_date()}.csv")
        df.to_csv(file_path, index=False)
        logging.info(f"Written {len(df)} lines to CSV: {file_path}")
        return df
    return None

def run():
    df = save_exchange_data()