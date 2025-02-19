import logging
from utils.file_handler import load_data, save_data

def check_balance(username):
    """Displays the user's balance."""
    data = load_data()
    print(f"Your balance: ${data[username]['balance']:.2f}")

def deposit(username):
    """Deposits money into the user's account."""
    data = load_data() # use class object
    
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid input.")
        return

    data[username]['balance'] += amount
    data[username]['transactions'].append(f"Deposited ${amount:.2f}")
    save_data(data)
    print(f"Successfully deposited ${amount:.2f}")
    logging.info(f"{username} deposited ${amount:.2f}")

def withdraw(username):
    """Withdraws money from the user's account."""
    data = load_data()

    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0 or amount > data[username]['balance']:
            print("Invalid or insufficient funds.")
            return
    except ValueError:
        print("Invalid input.")
        return

    data[username]['balance'] -= amount
    data[username]['transactions'].append(f"Withdrew ${amount:.2f}")
    save_data(data)
    print(f"Successfully withdrew ${amount:.2f}")
    logging.info(f"{username} withdrew ${amount:.2f}")

def transfer(username):
# def transfer(username: str) -> str: - edit this
    """Transfers money to another user."""
    data = load_data()
    recipient = input("Enter recipient username: ").strip()

    if recipient not in data or recipient == username:
        print("Invalid recipient.")
        return

    try:
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0 or amount > data[username]['balance']:
            print("Invalid or insufficient funds.")
            return
    except ValueError:
        print("Invalid input.")
        return

    data[username]['balance'] -= amount
    data[recipient]['balance'] += amount
    data[username]['transactions'].append(f"Transferred ${amount:.2f} to {recipient}")
    data[recipient]['transactions'].append(f"Received ${amount:.2f} from {username}")
    save_data(data)
    print(f"Successfully transferred ${amount:.2f} to {recipient}")
    logging.info(f"{username} transferred ${amount:.2f} to {recipient}")
