from account_management import AccountManagement

def main():
    system = AccountManagement()

    while True:
        # Print the menu options with a clear separation
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View Balance")
        print("4. Deposit Funds")
        print("5. Withdraw Funds")
        print("6. Transfer Funds")
        print("7. View Account Details")
        print("8. View All Accounts")
        print("9. Exit")
        print("--------------------------")

        # Get user input
        choice = input("Enter your choice: ")

        if choice == '1':
            # Option to create a new account
            owner = input("Enter account owner name: ")
            try:
                initial_deposit = float(input("Enter initial deposit: "))
                system.create_account(owner, initial_deposit)
                print("\nAccount created successfully.")
            except ValueError as e:
                print(f"\nError: {e}. Please enter a valid initial deposit.")

        elif choice == '2':
            # Option to delete an existing account
            owner = input("Enter account owner name to delete: ")
            try:
                system.delete_account(owner)
                print("\nAccount deleted successfully.")
            except ValueError as e:
                print(f"\nError: {e}")

        elif choice == '3':
            # Option to view balance of an account
            owner = input("Enter account owner name: ")
            account = system.get_account(owner)
            if account:
                print(f"\nBalance for {owner}: ₪{account.balance:.2f}")
            else:
                print("\nError: Account not found.")

        elif choice == '4':
            # Option to deposit funds into an account
            owner = input("Enter account owner name: ")
            try:
                amount = float(input("Enter deposit amount: "))
                account = system.get_account(owner)
                if account:
                    account.deposit(amount)
                    print("\nFunds deposited successfully.")
                else:
                    print("\nError: Account not found.")
            except ValueError as e:
                print(f"\nError: {e}. Please enter a valid deposit amount.")

        elif choice == '5':
            # Option to withdraw funds from an account
            owner = input("Enter account owner name: ")
            try:
                amount = float(input("Enter withdrawal amount: "))
                account = system.get_account(owner)
                if account:
                    account.withdraw(amount)
                    print("\nFunds withdrawn successfully.")
                else:
                    print("\nError: Account not found.")
            except ValueError as e:
                print(f"\nError: {e}. Please enter a valid withdrawal amount.")

        elif choice == '6':
            # Option to transfer funds between two accounts
            from_owner = input("Enter source account owner name: ")
            to_owner = input("Enter target account owner name: ")
            try:
                amount = float(input("Enter transfer amount: "))
                from_account = system.get_account(from_owner)
                to_account = system.get_account(to_owner)
                if from_account and to_account:
                    from_account.transfer(to_account, amount)
                    print("\nFunds transferred successfully.")
                else:
                    print("\nError: One or both accounts not found.")
            except ValueError as e:
                print(f"\nError: {e}. Please enter a valid transfer amount.")

        elif choice == '7':
            # Option to view details of an account
            owner = input("Enter account owner name: ")
            system.print_account_details(owner)

        elif choice == '8':
            # Option to view all accounts
            system.print_accounts()

        elif choice == '9':
            # Option to exit the system
            print("\nExiting system. Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("\nInvalid choice, please try again.")
            continue

        # Prompt user to continue or exit
        while True:
            continue_choice = input("\nDo you want to take another action? (1 for Yes, 9 for No): ")
            if continue_choice == '9':
                print("\nExiting system. Goodbye!")
                return
            elif continue_choice == '1':
                break
            else:
                print("\nInvalid choice, please enter 1 to continue or 9 to exit.")

if __name__ == "__main__":
    main()
