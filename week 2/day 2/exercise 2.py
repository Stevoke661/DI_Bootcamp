#bank account system
class BankAccount:
    def __init__(self, username, password, balance=0):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
        return self.authenticated

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to deposit.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        # Extend the parent init
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        # Check authentication first (inherited logic)
        if not self.authenticated:
            raise Exception("Authentication required.")
        
        # Override withdrawal logic for minimum balance
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Withdrawal denied. Must maintain a minimum balance of ${self.minimum_balance}")
        
        super().withdraw(amount) # Reuse the logic from parent
        
#Atm class
import sys

class ATM:
    def __init__(self, account_list, try_limit):
        # Validation: check if all items are bank accounts
        for acc in account_list:
            if not isinstance(acc, BankAccount):
                raise Exception("Account list must contain BankAccount instances.")
        
        self.account_list = account_list
        
        # Validation: try_limit
        try:
            if try_limit <= 0:
                raise ValueError
            self.try_limit = try_limit
        except (ValueError, TypeError):
            print("Invalid try limit. Setting default to 2.")
            self.try_limit = 2
        
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM MAIN MENU ---")
            print("1. Log In")
            print("2. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                user = input("Username: ")
                pw = input("Password: ")
                self.log_in(user, pw)
            elif choice == "2":
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid choice.")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                print(f"\nWelcome back, {username}!")
                self.current_tries = 0 # Reset tries on success
                self.show_account_menu(account)
                return

        # If no match found
        self.current_tries += 1
        print(f"Invalid credentials. Attempt {self.current_tries}/{self.try_limit}")
        
        if self.current_tries >= self.try_limit:
            print("Maximum tries reached. System shutting down.")
            sys.exit()

    def show_account_menu(self, account):
        while True:
            print("\n--- ACCOUNT MENU ---")
            print(f"Current Balance: ${account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Log Out")
            choice = input("Select an option: ")

            try:
                if choice == "1":
                    amt = int(input("Amount to deposit: "))
                    account.deposit(amt)
                elif choice == "2":
                    amt = int(input("Amount to withdraw: "))
                    account.withdraw(amt)
                elif choice == "3":
                    account.authenticated = False # Security reset
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice.")
            except Exception as e:
                print(f"Error: {e}")

# --- Testing the code ---
if __name__ == "__main__":
    acc1 = BankAccount("alice", "1234", 100)
    acc2 = MinimumBalanceAccount("bob", "5678", 500, 50)
    
    my_atm = ATM([acc1, acc2], 3)