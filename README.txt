
								Banking System
**Overview

This console-based banking system allows users to manage bank accounts with functionalities such as creating, deleting, depositing, withdrawing, 
transferring funds, and viewing account details. It is designed for simplicity and operates entirely in the console.
______________________

**Features:

-Create Account: Add a new account with an initial deposit.
-Delete Account: Remove an existing account.
-View Balance: Check the balance of an account.
-Deposit Funds: Deposit money into an account.
-Withdraw Funds: Withdraw money from an account.
-Transfer Funds: Transfer money between accounts.
-View Account Details: Display details and transaction history of a specific account.
-View All Accounts: List all accounts with their balances.
______________________

**Running the Application:

-Open Terminal or Command Prompt:
	Navigate to the directory containing the banking_app.py file.

-Run the Application:
	Execute the script using Python by running the following command: python banking_app.py

-Follow the On-Screen Instructions:
	The application will display a menu with options. Enter the corresponding number to choose an action.
_______________________

**Running Tests:

-Open Terminal or Command Prompt:
	Navigate to the directory containing the test files. (PythonQAFinal\proj)

-Run the Tests:
	Use the following commands to execute the tests with unittest: 1. python -m unittest .\test_account_management.py
								       2. python -m  unittest .\test_account.py
_______________________

**File Descriptions:

-account.py: Contains the Account class, which manages individual bank accounts, including methods for deposits, withdrawals, and transfers.

-account_management.py: Contains the AccountManagement class, which manages multiple accounts, allowing for account creation, deletion, and retrieval.

-banking_app.py: The main application script that provides a console-based interface for interacting with the banking system.

-test_account.py: Contains unit tests for the Account class.

-test_account_management.py: Contains unit tests for the AccountManagement class.
_______________________

**Example Usage:

-Create an Account:
	Enter 1 to create an account, then provide the owner’s name and initial deposit amount.

-Deposit Funds:
	Enter 4 to deposit funds, then specify the account owner and the amount to deposit.

-Withdraw Funds:
	Enter 5 to withdraw funds, then specify the account owner and the amount to withdraw.

-Transfer Funds:
	Enter 6 to transfer funds between accounts, then provide the source account, target account, and amount.

-View Account Details:
	Enter 7 to view details of an account, including transaction history.

-Exit the Application:
	Enter 9 to exit the application.
______________________