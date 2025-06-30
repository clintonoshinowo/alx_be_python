# bank_account.py

class BankAccount:
    """
    A simple BankAccount class to manage an account balance.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional initial balance.

        Args:
            initial_balance (float or int): The starting balance of the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            print("Warning: Initial balance must be a non-negative number. Setting to 0.")
            self._account_balance = 0.0
        else:
            self._account_balance = float(initial_balance) # Use a private attribute

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float or int): The amount to deposit.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit failed: Amount must be a positive number.")
            return False
        self._account_balance += amount
        return True

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float or int): The amount to withdraw.

        Returns:
            bool: True if withdrawal is successful, False otherwise (insufficient funds or invalid amount).
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal failed: Amount must be a positive number.")
            return False
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}") # Format to 2 decimal places
