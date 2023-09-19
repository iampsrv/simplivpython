class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type


class Account:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(amount, "Deposit")
        self.transactions.append(transaction)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = Transaction(amount, "Withdrawal")
            self.transactions.append(transaction)
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        account = Account(account_number, initial_balance)
        self.accounts[account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def get_all_accounts(self):
        return self.accounts.values()


def main():
    customers = {}

    while True:
        print("\n===== Bank Account Management System =====")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Display Transactions")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            customer = Customer(name, address)
            customers[name] = customer
            print("Customer created successfully!")

        elif choice == 2:
            customer_name = input("Enter customer name: ")
            account_number = int(input("Enter account number: "))
            initial_balance = float(input("Enter initial balance: "))

            if customer_name in customers:
                customer = customers[customer_name]
                customer.create_account(account_number, initial_balance)
                print("Account created successfully!")
            else:
                print("Customer not found!")

        elif choice == 3:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))

            for customer in customers.values():
                account = customer.get_account(account_number)
                if account:
                    account.deposit(amount)
                    print("Deposit successful!")
                    break
            else:
                print("Account not found!")

        elif choice == 4:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))

            for customer in customers.values():
                account = customer.get_account(account_number)
                if account:
                    account.withdraw(amount)
                    print("Withdrawal successful!")
                    break
            else:
                print("Account not found!")

        elif choice == 5:
            account_number = int(input("Enter account number: "))

            for customer in customers.values():
                account = customer.get_account(account_number)
                if account:
                    print(f"Account balance: {account.get_balance()}")
                    break
            else:
                print("Account not found!")

        elif choice == 6:
            account_number = int(input("Enter account number: "))

            for customer in customers.values():
                account = customer.get_account(account_number)
                if account:
                    transactions = account.get_transactions()
                    print("\n===== Transactions =====")
                    for transaction in transactions:
                        print(f"{transaction.transaction_type}: {transaction.amount}")
                    break
            else:
                print("Account not found!")

        elif choice == 7:
            print("Thank you for using the Bank Account Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
