import logging
import json
import os
from datetime import datetime

class CustomFormatter(logging.Formatter):
    """
    Custom logging formatter to include milliseconds in the timestamp.
    """
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created)
        return dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Keeps 3 decimal places for milliseconds

def configure_logging():
    """
    Configures logging to write to a file.
    - Logs are written to 'exchange.log' with DEBUG level.
    - The log format includes timestamp, log level, and message.
    """
    log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
    formatter = CustomFormatter(log_format)

    # File handler to write logs to 'exchange.log'
    file_handler = logging.FileHandler("exchange.log", mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # Logs all messages (DEBUG and above)
    file_handler.setFormatter(formatter)

    # Apply handler to the root logger
    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler])

def load_config():
    """
    Loads API configuration from a JSON file.
    - If 'config.json' exists, it loads the settings.
    - If the file is missing, it logs a warning and returns default settings.
    """
    config_file = "config/config.json"
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return json.load(file)
    logging.warning("Config file not found. Using defaults.")
    return {"base_url": "https://api.coingecko.com/api/v3/"}  # Default API URL

def current_date():
    """
    Returns the current date formatted as YYYYMMDD (e.g., '20250309' for March 9, 2025).
    """
    return datetime.now().strftime('%Y%m%d')