import math

# Bank Account class
class BankAccount:
    def __init__(self, account_holder_name, account_number, initial_deposit):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited: {amount}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Successfully withdrew: {amount}"
        return "Insufficient balance or invalid withdrawal amount."

    def display_account_details(self):
        return f"Account Holder: {self.account_holder_name}, Account Number: {self.account_number}, Balance: {self.balance}"

# Fixed Deposit Account class
class FixedDepositAccount(BankAccount):
    def __init__(self, account_holder_name, account_number, deposit, duration_in_years, interest_rate):
        super().__init__(account_holder_name, account_number, deposit)
        self.duration_in_years = duration_in_years
        self.interest_rate = interest_rate

    def calculate_maturity_amount(self):
        return self.balance * math.pow(1 + self.interest_rate / 100, self.duration_in_years)

    def display_fixed_deposit_details(self):
        details = super().display_account_details()
        maturity_amount = self.calculate_maturity_amount()
        return f"{details}, Duration: {self.duration_in_years} years, Interest Rate: {self.interest_rate}%, Maturity Amount: {maturity_amount:.2f}"

# Loan Account class
class LoanAccount:
    def __init__(self, borrower_name, loan_account_number, loan_amount, interest_rate, duration_in_years):
        self.borrower_name = borrower_name
        self.loan_account_number = loan_account_number
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.duration_in_years = duration_in_years

    def calculate_total_payable(self):
        return self.loan_amount * math.pow(1 + self.interest_rate / 100, self.duration_in_years)

    def display_loan_details(self):
        total_payable = self.calculate_total_payable()
        return f"Borrower Name: {self.borrower_name}, Loan Account Number: {self.loan_account_number}, Loan Amount: {self.loan_amount}, Interest Rate: {self.interest_rate}%, Duration: {self.duration_in_years} years, Total Payable Amount: {total_payable:.2f}"

# Main Banking Management System
class BankingManagementSystem:
    def __init__(self):
        self.accounts = []
        self.fixed_deposits = []
        self.loans = []

    def create_account(self, name, initial_deposit):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(initial_deposit, (int, float)) or initial_deposit <= 0:
            raise ValueError("Initial deposit must be a positive number.")
        account_number = 1000 + len(self.accounts) + 1
        account = BankAccount(name, account_number, initial_deposit)
        self.accounts.append(account)
        return f"Account created successfully! Account Number: {account_number}"



    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.deposit(amount)
        return "Account not found."

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.withdraw(amount)
        return "Account not found."

    def create_fixed_deposit(self, name, deposit, duration_in_years, interest_rate):
        account_number = 2000 + len(self.fixed_deposits) + 1
        fd_account = FixedDepositAccount(name, account_number, deposit, duration_in_years, interest_rate)
        self.fixed_deposits.append(fd_account)
        return fd_account.display_fixed_deposit_details()

    def apply_for_loan(self, name, loan_amount, interest_rate, duration_in_years):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(loan_amount, (int, float)) or loan_amount <= 0:
            raise ValueError("Loan amount must be a positive number.")
        if not isinstance(interest_rate, (int, float)) or interest_rate <= 0:
            raise ValueError("Interest rate must be a positive number.")
        if not isinstance(duration_in_years, int) or duration_in_years <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        loan_account_number = 3000 + len(self.loans) + 1
        loan_account = LoanAccount(name, loan_account_number, loan_amount, interest_rate, duration_in_years)
        self.loans.append(loan_account)
        return loan_account.display_loan_details()


    def display_all_accounts(self):
        return [account.display_account_details() for account in self.accounts]

# Sample Test Cases
def test_banking_system():
    bms = BankingManagementSystem()

    # Test creating accounts
    print(bms.create_account("Alice", 1000))
    print(bms.create_account("Bob", 5000))

    # Test depositing money
    print(bms.deposit(1001, 500))
    print(bms.deposit(9999, 300))  # Invalid account number

    # Test withdrawing money
    print(bms.withdraw(1001, 200))
    print(bms.withdraw(1001, 2000))  # Insufficient funds

    # Test fixed deposit
    print(bms.create_fixed_deposit("Alice", 10000, 5, 6.5))

    # Test applying for a loan
    print(bms.apply_for_loan("Charlie", 50000, 10, 2))

    # Display all accounts
    print("\nAll Accounts:")
    print("\n".join(bms.display_all_accounts()))

# Run the test
test_banking_system()
