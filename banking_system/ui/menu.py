from services.auth import register, login
from services.transactions import check_balance, deposit, withdraw, transfer

def main_menu():
    """Displays the main menu."""
    while True:
        print("\nBanking System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Logout")
                    sub_choice = input("Enter choice: ").strip()
                    
                    if sub_choice == '1':
                        check_balance(user)
                    elif sub_choice == '2':
                        deposit(user)
                    elif sub_choice == '3':
                        withdraw(user)
                    elif sub_choice == '4':
                        transfer(user)
                    elif sub_choice == '5':
                        break
                    else:
                        print("Invalid choice!")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
