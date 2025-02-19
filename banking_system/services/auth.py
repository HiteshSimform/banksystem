import logging
from utils.file_handler import load_data, save_data
from utils.security import hash_password, verify_password

def register():
    """Registers a new user."""
    data = load_data()
    
    while True:
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty.")
            continue
        if username in data:
            print("User already exists!")
            continue
        break

    while True:
        password = input("Enter password: ").strip()
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        confirm_password = input("Confirm password: ").strip()
        if password != confirm_password:
            print("Passwords do not match.")
            continue
        break

    data[username] = {"password": hash_password(password), "balance": 0.0, "transactions": []}
    save_data(data)
    print("Registration successful!")
    logging.info(f"User registered: {username}")

def login():
    """Logs in a user."""
    data = load_data()
    username = input("Enter username: ").strip()
    
    if username not in data:
        print("Invalid username or password!")
        return None

    password = input("Enter password: ").strip()
    if verify_password(password, data[username]['password']):
        print(f"Welcome {username}!")
        logging.info(f"User logged in: {username}")
        return username
    else:
        print("Invalid username or password!")
        return None
