from datetime import datetime

class Account:
    def __init__(self, owner, initial_deposit=0):
        """
        Initializes an account with the given owner and initial deposit.
        Adds an initial transaction for the initial deposit.
        Parameters:
        - owner (str): The name of the account owner.
        - initial_deposit (float): The initial deposit amount.
        """
        self.owner = owner
        self.balance = initial_deposit
        self.transactions = []
        self.add_transaction('Initial deposit', initial_deposit)

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        Parameters:
        - amount (float): The amount to be deposited.
        Raises:
        - ValueError: If the deposit amount is zero or negative.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.add_transaction('Deposit', amount)

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.
        Parameters:
        - amount (float): The amount to be withdrawn.
        Raises:
        - ValueError: If the withdrawal amount exceeds the current balance or is zero or negative.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.add_transaction('Withdrawal', -amount)

    def transfer(self, target_account, amount):
        """
        Transfers a specified amount from this account to the target account.
        Parameters:
        - target_account (Account): The account to which the amount will be transferred.
        - amount (float): The amount to be transferred.
        Raises:
        - ValueError: If the transfer amount is zero or negative, or if there are insufficient funds.
        """
        if self.owner == target_account.owner:
            raise ValueError("You can't transfer to yourself! Please choose a valid target.")
        self.withdraw(amount)
        target_account.deposit(amount)
        self.add_transaction(f'Transferred to {target_account.owner}', -amount)
        target_account.add_transaction(f'Received from {self.owner}', amount)

    def add_transaction(self, description, amount):
        """
        Adds a transaction to the transaction history.
        Parameters:
        - description (str): The description of the transaction.
        - amount (float): The amount of the transaction.
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transactions.append({'timestamp': timestamp, 'description': description, 'amount': amount})

    def get_transaction_history(self):
        """
        Retrieves the transaction history of the account.
        Returns:
        - list: A list of transactions, where each transaction is a dictionary.
        """
        return self.transactions

    def print_transaction_history(self):
        """
        Prints the transaction history of the account.
        """
        for transaction in self.transactions:
            print(f"{transaction['timestamp']} - {transaction['description']}: {transaction['amount']}")
