import tkinter as tk
from tkinter import messagebox, simpledialog
import math
import csv
import os


# Bank Account class
class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance
        self.transactions = [f"Account created with initial deposit: {balance}"]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            return f"Successfully deposited: {amount}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            return f"Successfully withdrew: {amount}"
        return "Insufficient balance or invalid withdrawal amount."

    def get_transaction_history(self):
        return "\n".join(self.transactions)


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
        return (
            f"Loan ID: {self.loan_account_number}, Loan Amount: {self.loan_amount}, "
            f"Interest Rate: {self.interest_rate}%, Duration: {self.duration_in_years} years, "
            f"Total Payable: {total_payable:.2f}"
        )


class BankingManagementSystem:
    def __init__(self, account_db="accounts.csv", loan_db="loans.csv"):
        self.accounts = []
        self.loans = []
        self.account_db = account_db
        self.loan_db = loan_db
        self.load_accounts()
        self.load_loans()

    def load_accounts(self):
        """Load accounts from the CSV database."""
        if not os.path.exists(self.account_db):
            return

        with open(self.account_db, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                account = BankAccount(
                    row["account_holder_name"],
                    int(row["account_number"]),
                    float(row["balance"]),
                )
                self.accounts.append(account)

    def save_accounts(self):
        """Save all accounts to the CSV database."""
        with open(self.account_db, mode="w", newline="") as file:
            fieldnames = ["account_holder_name", "account_number", "balance"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for account in self.accounts:
                writer.writerow(
                    {
                        "account_holder_name": account.account_holder_name,
                        "account_number": account.account_number,
                        "balance": account.balance,
                    }
                )

    def load_loans(self):
        """Load loans from the CSV database."""
        if not os.path.exists(self.loan_db):
            return

        with open(self.loan_db, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                loan = LoanAccount(
                    row["borrower_name"],
                    int(row["loan_account_number"]),
                    float(row["loan_amount"]),
                    float(row["interest_rate"]),
                    int(row["duration_in_years"]),
                )
                self.loans.append(loan)

    def save_loans(self):
        """Save all loans to the CSV database."""
        with open(self.loan_db, mode="w", newline="") as file:
            fieldnames = [
                "borrower_name",
                "loan_account_number",
                "loan_amount",
                "interest_rate",
                "duration_in_years",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for loan in self.loans:
                writer.writerow(
                    {
                        "borrower_name": loan.borrower_name,
                        "loan_account_number": loan.loan_account_number,
                        "loan_amount": loan.loan_amount,
                        "interest_rate": loan.interest_rate,
                        "duration_in_years": loan.duration_in_years,
                    }
                )

    def create_account(self, name, initial_deposit):
        account_number = 1000 + len(self.accounts) + 1
        account = BankAccount(name, account_number, initial_deposit)
        self.accounts.append(account)
        self.save_accounts()  # Save changes to the database
        return f"Account created successfully! Account Number: {account_number}"

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                self.save_accounts()  # Save changes to the database
                return f"Account {account_number} deleted successfully."
        return "Account not found."

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def display_all_accounts(self):
        return "\n".join(
            [
                f"Account Holder: {account.account_holder_name}, Account Number: {account.account_number}, Balance: {account.balance}"
                for account in self.accounts
            ]
        )

    def apply_for_loan(self, borrower_name, loan_amount, interest_rate, duration_in_years):
        loan_account_number = 3000 + len(self.loans) + 1
        loan = LoanAccount(borrower_name, loan_account_number, loan_amount, interest_rate, duration_in_years)
        self.loans.append(loan)
        self.save_loans()  # Save changes to the database
        return loan.display_loan_details()

    def get_loans_by_borrower(self, borrower_name):
        return [loan for loan in self.loans if loan.borrower_name == borrower_name]


# Customer Portal
class CustomerPortal:
    def __init__(self, root, system, account):
        self.system = system
        self.account = account
        self.root = root
        self.root.title("Customer Portal - Banking Management System")
        self.root.geometry("600x600")

        tk.Label(root, text=f"Welcome, {account.account_holder_name}", font=("Helvetica", 18, "bold")).grid(row=0, columnspan=2, pady=20)

        tk.Button(root, text="Deposit", command=self.deposit).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(root, text="Withdraw", command=self.withdraw).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Apply for Loan", command=self.apply_for_loan).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(root, text="View Loans", command=self.view_loans).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(root, text="View Transactions", command=self.view_transactions).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="Logout", command=self.logout).grid(row=3, column=1, pady=20)

    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter Deposit Amount:")
        if amount:
            result = self.account.deposit(amount)
            self.system.save_accounts()  # Save changes to the database
            messagebox.showinfo("Result", result)

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter Withdraw Amount:")
        if amount:
            result = self.account.withdraw(amount)
            self.system.save_accounts()  # Save changes to the database
            messagebox.showinfo("Result", result)

    def apply_for_loan(self):
        loan_amount = simpledialog.askfloat("Loan Application", "Enter Loan Amount:")
        interest_rate = simpledialog.askfloat("Loan Application", "Enter Interest Rate:")
        duration = simpledialog.askinteger("Loan Application", "Enter Duration (in years):")
        if loan_amount and interest_rate and duration:
            result = self.system.apply_for_loan(self.account.account_holder_name, loan_amount, interest_rate, duration)
            messagebox.showinfo("Loan Approved", result)

    def view_loans(self):
        loans = self.system.get_loans_by_borrower(self.account.account_holder_name)
        if loans:
            loan_details = "\n".join([loan.display_loan_details() for loan in loans])
            messagebox.showinfo("Your Loans", loan_details)
        else:
            messagebox.showinfo("Your Loans", "No loans found.")

    def view_transactions(self):
        history = self.account.get_transaction_history()
        messagebox.showinfo("Transaction History", history)

    def logout(self):
        self.root.destroy()
        main()

# Admin GUI
class AdminPortal:
    def __init__(self, root, system):
        self.system = system
        self.root = root
        self.root.title("Admin Portal - Banking Management System")
        self.root.geometry("600x500")

        # Admin Controls
        tk.Label(root, text="Admin Portal", font=("Helvetica", 18, "bold")).grid(row=0, columnspan=2, pady=20)

        tk.Button(root, text="Create Account", command=self.create_account).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(root, text="View All Accounts", command=self.display_all_accounts).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Logout", command=self.logout).grid(row=2, columnspan=2, padx=10, pady=10)

    def create_account(self):
        name = simpledialog.askstring("Create Account", "Enter Account Holder Name:")
        initial_deposit = simpledialog.askfloat("Create Account", "Enter Initial Deposit:")
        if name and initial_deposit:
            result = self.system.create_account(name, initial_deposit)
            messagebox.showinfo("Success", result)

    def display_all_accounts(self):
        result = self.system.display_all_accounts()
        messagebox.showinfo("Accounts", result if result else "No accounts available.")

    def logout(self):
        self.root.destroy()
        main()


# Starting Window
def main():
    root = tk.Tk()
    root.title("Banking Management System")
    root.geometry("400x300")

    system = BankingManagementSystem()

    tk.Label(root, text="Bank Management System", font=("Helvetica", 16, "bold")).pack(pady=20)

    tk.Button(root, text="Login as Admin", command=lambda: admin_login(root, system), width=20).pack(pady=10)
    tk.Button(root, text="Login as Customer", command=lambda: customer_login(root, system), width=20).pack(pady=10)

    root.mainloop()


def admin_login(root, system):
    password = simpledialog.askstring("Admin Login", "Enter Admin Password:", show="*")
    if password == "admin123":
        root.destroy()
        root = tk.Tk()
        AdminPortal(root, system)
    else:
        messagebox.showerror("Error", "Invalid Admin Password")


def customer_login(root, system):
    account_number = simpledialog.askinteger("Customer Login", "Enter Account Number:")
    account = system.get_account(account_number)
    if account:
        root.destroy()
        root = tk.Tk()
        CustomerPortal(root, system, account)
    else:
        messagebox.showerror("Error", "Account not found")


if __name__ == "__main__":
    main()

