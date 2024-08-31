from account import Account


class AccountManagement:
    """
    Manages a collection of bank accounts and provides methods for
    account creation, deletion, and management.
    """

    def __init__(self):
        """
        Initializes an empty banking system.
        """
        self.accounts = {}

    def create_account(self, owner, initial_deposit):
        """
        Creates a new account with the given owner name and initial deposit.
        Parameters:
        - owner (str): The name of the account owner.
        - initial_deposit (float): The initial deposit amount.
        Raises:
        - ValueError: If an account with the given owner name already exists,
          if the owner name is empty, or if the initial deposit is negative.
        """
        if not owner.strip():
            raise ValueError("Account owner name cannot be empty.")
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        if owner in self.accounts:
            raise ValueError("Account already exists.")

        self.accounts[owner] = Account(owner, initial_deposit)

    def delete_account(self, owner):
        """
        Deletes an existing account with the given owner name.
        Parameters:
        - owner (str): The name of the account owner to be deleted.
        Raises:
        - ValueError: If no account with the given owner name exists or if
          the owner name is empty.
        """
        if not owner.strip():
            raise ValueError("Account owner name cannot be empty.")
        if owner not in self.accounts:
            raise ValueError("Account not found.")

        del self.accounts[owner]

    def get_account(self, owner):
        """
        Retrieves the account for the given owner name.
        Parameters:
        - owner (str): The name of the account owner.
        Returns:
        - Account: The account associated with the given owner name.
        Raises:
        - ValueError: If the account does not exist or if the owner name is empty.
        """
        if not owner.strip():
            raise ValueError("Account owner name cannot be empty.")
        return self.accounts.get(owner, None)

    def print_accounts(self):
        """
        Prints all of the accounts found in the system. If none are found, prints "No accounts found.".
        """
        if not self.accounts:
            print("No accounts found.")
        else:
            for owner, account in self.accounts.items():
                print(f"Owner: {owner}, Balance: {account.balance}")

    def print_account_details(self, owner):
        """
        Prints the details of a specific account, including balance and transaction history.
        Parameters:
        - owner (str): The name of the account owner.
        Raises:
        - ValueError: If the account is not found.
        """
        account = self.get_account(owner)
        if account:
            print(f"Owner: {account.owner}")
            print(f"Balance: {account.balance}")
            print("-Transaction History:")
            account.print_transaction_history()
        else:
            print("Account not found.")
