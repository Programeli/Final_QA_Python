import unittest
from account_management import AccountManagement
from unittest.mock import patch

class TestAccountManagement(unittest.TestCase):

    def setUp(self):
        """
        Initializes the AccountManagement system before each test.
        """
        self.system = AccountManagement()

    def test_create_account(self):
        """
        Test that a new account is created successfully.
        """
        owner = "Elias T"
        initial_deposit = 1000.0
        self.system.create_account(owner, initial_deposit)
        account = self.system.get_account(owner)
        self.assertIsNotNone(account)
        self.assertEqual(account.balance, initial_deposit)

    def test_create_account_duplicate(self):
        """
        Test that creating an account with a duplicate owner raises a ValueError.
        """
        owner = "Tuma E"
        self.system.create_account(owner, 500)
        with self.assertRaises(ValueError):
            self.system.create_account(owner, 300)

    def test_delete_account(self):
        """
        Test that an account is deleted successfully.
        """
        owner = "Elias T"
        self.system.create_account(owner, 1000)
        self.system.delete_account(owner)
        account = self.system.get_account(owner)
        self.assertIsNone(account)

    def test_delete_account_not_found(self):
        """
        Test that deleting a non-existent account raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.system.delete_account("Nonexistent Account")

    def test_deposit_funds(self):
        """
        Test that depositing funds into an account increases the balance correctly.
        """
        owner = "Elias T"
        self.system.create_account(owner, 500)
        account = self.system.get_account(owner)
        account.deposit(200)
        self.assertEqual(account.balance, 700)

    def test_withdraw_funds(self):
        """
        Test that withdrawing funds from an account decreases the balance correctly.
        """
        owner = "Elias T"
        self.system.create_account(owner, 1000)
        account = self.system.get_account(owner)
        account.withdraw(300)
        self.assertEqual(account.balance, 700)

    def test_withdraw_insufficient_funds(self):
        """
        Test that attempting to withdraw more than the balance raises a ValueError.
        """
        owner = "Elias T"
        self.system.create_account(owner, 500)
        account = self.system.get_account(owner)
        with self.assertRaises(ValueError):
            account.withdraw(600)

    def test_transfer_funds(self):
        """
        Test that transferring funds between accounts updates both accounts' balances correctly.
        """
        owner1 = "Elias T"
        owner2 = "Tuma E"
        self.system.create_account(owner1, 1000)
        self.system.create_account(owner2, 500)
        account1 = self.system.get_account(owner1)
        account2 = self.system.get_account(owner2)
        account1.transfer(account2, 300)
        self.assertEqual(account1.balance, 700)
        self.assertEqual(account2.balance, 800)

    def test_transfer_insufficient_funds(self):
        """
        Test that transferring more funds than available in the source account raises a ValueError.
        """
        owner1 = "Elias T"
        owner2 = "Tuma E"
        self.system.create_account(owner1, 500)
        self.system.create_account(owner2, 1000)
        account1 = self.system.get_account(owner1)
        account2 = self.system.get_account(owner2)
        with self.assertRaises(ValueError):
            account1.transfer(account2, 600)

    def test_view_account_details(self):
        """
        Test that viewing an account's details returns the correct information.
        """
        owner = "Elias T"
        initial_deposit = 1500
        self.system.create_account(owner, initial_deposit)
        account = self.system.get_account(owner)
        # Check that owner and balance are correct
        self.assertEqual(account.owner, owner)
        self.assertEqual(account.balance, initial_deposit)

    def test_view_all_accounts(self):
        """
        Test that all accounts are printed correctly.
        """
        self.system.create_account("Elias T", 1000)
        self.system.create_account("Tuma E", 1500)
        accounts = self.system.accounts
        self.assertEqual(len(accounts), 2)
        self.assertIn("Elias T", accounts)
        self.assertIn("Tuma E", accounts)

    @patch('builtins.print')
    def test_print_no_accounts(self, mock_print):
        """
        Test that printing accounts when there are none outputs the correct message.
        """
        system = AccountManagement()
        system.print_accounts()
        mock_print.assert_called_with("No accounts found.")

if __name__ == '__main__':
    unittest.main()
