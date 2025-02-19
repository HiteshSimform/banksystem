import os
import json
import logging

DATA_FILE = "bank_data.json"

def load_data():
    """Loads user data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.error("Error loading data. File might be corrupted.")
        return {}

def save_data(data):
    """Saves user data to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        logging.error(f"Failed to save data: {e}")
