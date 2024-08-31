import unittest
from account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        """
        Set up an initial account for testing with a starting balance of 1000.
        """
        self.account = Account('Eli Tum', 1000)

    def test_create_account(self):
        """
        Test that the account is created with the correct owner and balance.
        """
        self.assertEqual(self.account.owner, 'Eli Tum')
        self.assertEqual(self.account.balance, 1000)

    def test_deposit_funds(self):
        """
        Test depositing funds into the account and ensure the balance updates correctly.
        """
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw_funds(self):
        """
        Test withdrawing funds from the account with sufficient balance.
        """
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_withdraw_insufficient_funds(self):
        """
        Test withdrawing funds when there is not enough balance, expecting a ValueError.
        """
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_transfer_funds(self):
        """
        Test transferring funds between two accounts and ensure both balances are updated correctly.
        """
        account2 = Account('Tum Eli', 500)
        self.account.transfer(account2, 200)
        self.assertEqual(self.account.balance, 800)
        self.assertEqual(account2.balance, 700)

    def test_deposit_zero_or_negative_amount(self):
        """
        Test depositing zero or negative amounts, expecting a ValueError.
        """
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_zero_or_negative_amount(self):
        """
        Test withdrawing zero or negative amounts, expecting a ValueError.
        """
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_transaction_history_updates(self):
        """
        Test that transaction history updates correctly after deposits, withdrawals, and transfers.
        """
        # Resetting the account for fresh history
        self.account = Account('Eli Tum', 1000)

        # Deposit funds and check history
        self.account.deposit(500)
        self.assertEqual(len(self.account.get_transaction_history()), 2)  # Initial deposit + one deposit

        # Withdraw funds and check history
        self.account.withdraw(200)
        self.assertEqual(len(self.account.get_transaction_history()), 3)  # Two previous transactions + one withdrawal

        # Transfer funds to another account and check history
        account2 = Account('Tum Eli', 500)
        self.account.transfer(account2, 100)
        self.assertEqual(len(self.account.get_transaction_history()), 5)  # Three previous transactions + one transfer

        # Check the transactions in history
        transactions = self.account.get_transaction_history()
        self.assertEqual(transactions[-1]['description'], 'Transferred to Tum Eli')
        self.assertEqual(transactions[-1]['amount'], -100)

    def test_transfer_to_self(self):
        """
        Test that transferring funds to the same account raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.account.transfer(self.account, 100)
        self.assertEqual(str(context.exception), "You can't transfer to yourself! Please choose a valid target.")


if __name__ == '__main__':
    unittest.main()
