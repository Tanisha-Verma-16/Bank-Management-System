# import tkinter as tk
# from tkinter import messagebox
# import math

# # Banking Management System Classes (as provided earlier)

# class BankAccount:
#     def __init__(self, account_holder_name, account_number, initial_deposit):
#         self.account_holder_name = account_holder_name
#         self.account_number = account_number
#         self.balance = initial_deposit

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"Successfully deposited: {amount}"
#         return "Invalid deposit amount."

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"Successfully withdrew: {amount}"
#         return "Insufficient balance or invalid withdrawal amount."

#     def display_account_details(self):
#         return f"Account Holder: {self.account_holder_name}, Account Number: {self.account_number}, Balance: {self.balance}"


# class BankingManagementSystem:
#     def __init__(self):
#         self.accounts = []

#     def create_account(self, name, initial_deposit):
#         account_number = 1000 + len(self.accounts) + 1
#         account = BankAccount(name, account_number, initial_deposit)
#         self.accounts.append(account)
#         return f"Account created successfully! Account Number: {account_number}"

#     def deposit(self, account_number, amount):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account.deposit(amount)
#         return "Account not found."

#     def withdraw(self, account_number, amount):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account.withdraw(amount)
#         return "Account not found."

#     def display_all_accounts(self):
#         return "\n".join([account.display_account_details() for account in self.accounts])


# # GUI Implementation
# class BankingGUI:
#     def __init__(self, root, system):
#         self.system = system
#         self.root = root
#         self.root.title("Banking Management System")

#         # Account creation
#         tk.Label(root, text="Account Holder Name:").grid(row=0, column=0)
#         self.name_entry = tk.Entry(root)
#         self.name_entry.grid(row=0, column=1)

#         tk.Label(root, text="Initial Deposit:").grid(row=1, column=0)
#         self.deposit_entry = tk.Entry(root)
#         self.deposit_entry.grid(row=1, column=1)

#         tk.Button(root, text="Create Account", command=self.create_account).grid(row=2, columnspan=2)

#         # Deposit
#         tk.Label(root, text="Account Number (Deposit):").grid(row=3, column=0)
#         self.deposit_acc_entry = tk.Entry(root)
#         self.deposit_acc_entry.grid(row=3, column=1)

#         tk.Label(root, text="Deposit Amount:").grid(row=4, column=0)
#         self.deposit_amount_entry = tk.Entry(root)
#         self.deposit_amount_entry.grid(row=4, column=1)

#         tk.Button(root, text="Deposit", command=self.deposit).grid(row=5, columnspan=2)

#         # Withdraw
#         tk.Label(root, text="Account Number (Withdraw):").grid(row=6, column=0)
#         self.withdraw_acc_entry = tk.Entry(root)
#         self.withdraw_acc_entry.grid(row=6, column=1)

#         tk.Label(root, text="Withdraw Amount:").grid(row=7, column=0)
#         self.withdraw_amount_entry = tk.Entry(root)
#         self.withdraw_amount_entry.grid(row=7, column=1)

#         tk.Button(root, text="Withdraw", command=self.withdraw).grid(row=8, columnspan=2)

#         # Display Accounts
#         tk.Button(root, text="Display All Accounts", command=self.display_accounts).grid(row=9, columnspan=2)

#     def create_account(self):
#         name = self.name_entry.get()
#         try:
#             initial_deposit = float(self.deposit_entry.get())
#             result = self.system.create_account(name, initial_deposit)
#             messagebox.showinfo("Success", result)
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid amount.")

#     def deposit(self):
#         try:
#             account_number = int(self.deposit_acc_entry.get())
#             amount = float(self.deposit_amount_entry.get())
#             result = self.system.deposit(account_number, amount)
#             messagebox.showinfo("Result", result)
#         except ValueError:
#             messagebox.showerror("Error", "Please enter valid details.")

#     def withdraw(self):
#         try:
#             account_number = int(self.withdraw_acc_entry.get())
#             amount = float(self.withdraw_amount_entry.get())
#             result = self.system.withdraw(account_number, amount)
#             messagebox.showinfo("Result", result)
#         except ValueError:
#             messagebox.showerror("Error", "Please enter valid details.")

#     def display_accounts(self):
#         result = self.system.display_all_accounts()
#         messagebox.showinfo("Accounts", result if result else "No accounts available.")


# # Main execution
# if __name__ == "__main__":
#     root = tk.Tk()
#     system = BankingManagementSystem()
#     gui = BankingGUI(root, system)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import math


# # Bank Account class
# class BankAccount:
#     def __init__(self, account_holder_name, account_number, initial_deposit):
#         self.account_holder_name = account_holder_name
#         self.account_number = account_number
#         self.balance = initial_deposit

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"Successfully deposited: {amount}"
#         return "Invalid deposit amount."

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"Successfully withdrew: {amount}"
#         return "Insufficient balance or invalid withdrawal amount."

#     def display_account_details(self):
#         return f"Account Holder: {self.account_holder_name}, Account Number: {self.account_number}, Balance: {self.balance}"


# class BankingManagementSystem:
#     def __init__(self):
#         self.accounts = []

#     def create_account(self, name, initial_deposit):
#         account_number = 1000 + len(self.accounts) + 1
#         account = BankAccount(name, account_number, initial_deposit)
#         self.accounts.append(account)
#         return f"Account created successfully! Account Number: {account_number}"

#     def deposit(self, account_number, amount):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account.deposit(amount)
#         return "Account not found."

#     def withdraw(self, account_number, amount):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account.withdraw(amount)
#         return "Account not found."

#     def display_all_accounts(self):
#         return "\n".join([account.display_account_details() for account in self.accounts])

#     def delete_account(self, account_number):
#         for account in self.accounts:
#             if account.account_number == account_number:
#                 self.accounts.remove(account)
#                 return f"Account {account_number} deleted successfully."
#         return "Account not found."


# # Admin GUI
# class AdminPortal:
#     def __init__(self, root, system):
#         self.system = system
#         self.root = root
#         self.root.title("Admin Portal - Banking Management System")
#         self.root.geometry("800x600")  # Enlarged window size

#         tk.Label(root, text="Enter Admin Password:").grid(row=0, column=0, pady=10)
#         self.password_entry = tk.Entry(root, show="*")
#         self.password_entry.grid(row=0, column=1, pady=10)

#         tk.Button(root, text="Login", command=self.admin_login).grid(row=1, columnspan=2, pady=10)

#     def admin_login(self):
#         password = self.password_entry.get()
#         if password == "admin123":  # Simple password validation
#             self.load_admin_panel()
#         else:
#             messagebox.showerror("Access Denied", "Incorrect Password.")

#     def load_admin_panel(self):
#         # Clear previous widgets
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Admin Controls
#         tk.Label(self.root, text="Admin Portal", font=("Helvetica", 18, "bold")).grid(row=0, columnspan=2, pady=20)

#         tk.Button(self.root, text="Create Account", command=self.create_account).grid(row=1, column=0, padx=10, pady=10)
#         tk.Button(self.root, text="View All Accounts", command=self.display_all_accounts).grid(row=1, column=1, padx=10, pady=10)
#         tk.Button(self.root, text="Delete Account", command=self.delete_account).grid(row=2, column=0, padx=10, pady=10)
#         tk.Button(self.root, text="Logout", command=self.logout).grid(row=2, column=1, padx=10, pady=10)

#     def create_account(self):
#         AccountCreationWindow(self.root, self.system)

#     def display_all_accounts(self):
#         result = self.system.display_all_accounts()
#         messagebox.showinfo("Accounts", result if result else "No accounts available.")

#     def delete_account(self):
#         account_number = tk.simpledialog.askinteger("Delete Account", "Enter Account Number:")
#         if account_number:
#             result = self.system.delete_account(account_number)
#             messagebox.showinfo("Result", result)

#     def logout(self):
#         self.root.destroy()
#         main()


# class AccountCreationWindow:
#     def __init__(self, root, system):
#         self.system = system
#         self.top = tk.Toplevel(root)
#         self.top.title("Create Account")
#         self.top.geometry("400x300")

#         tk.Label(self.top, text="Account Holder Name:").grid(row=0, column=0, pady=10)
#         self.name_entry = tk.Entry(self.top)
#         self.name_entry.grid(row=0, column=1, pady=10)

#         tk.Label(self.top, text="Initial Deposit:").grid(row=1, column=0, pady=10)
#         self.deposit_entry = tk.Entry(self.top)
#         self.deposit_entry.grid(row=1, column=1, pady=10)

#         tk.Button(self.top, text="Create Account", command=self.create_account).grid(row=2, columnspan=2, pady=20)

#     def create_account(self):
#         name = self.name_entry.get()
#         try:
#             initial_deposit = float(self.deposit_entry.get())
#             result = self.system.create_account(name, initial_deposit)
#             messagebox.showinfo("Success", result)
#             self.top.destroy()
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid deposit amount.")


# # Main Application
# def main():
#     root = tk.Tk()
#     system = BankingManagementSystem()
#     app = AdminPortal(root, system)
#     root.mainloop()


# if __name__ == "__main__":
#     main()


import tkinter as tk
from tkinter import messagebox, simpledialog
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
        return f"Borrower Name: {self.borrower_name}, Loan Amount: {self.loan_amount}, Interest Rate: {self.interest_rate}%, Total Payable: {total_payable:.2f}"


class BankingManagementSystem:
    def __init__(self):
        self.accounts = []
        self.loans = []

    def create_account(self, name, initial_deposit):
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

    def display_all_accounts(self):
        return "\n".join([account.display_account_details() for account in self.accounts])

    def apply_for_loan(self, borrower_name, loan_amount, interest_rate, duration_in_years):
        loan_account_number = 3000 + len(self.loans) + 1
        loan = LoanAccount(borrower_name, loan_account_number, loan_amount, interest_rate, duration_in_years)
        self.loans.append(loan)
        return loan.display_loan_details()


# Customer GUI
class CustomerPortal:
    def __init__(self, root, system):
        self.system = system
        self.root = root
        self.root.title("Customer Portal - Banking Management System")
        self.root.geometry("600x500")

        # Customer Controls
        tk.Label(root, text="Customer Portal", font=("Helvetica", 18, "bold")).grid(row=0, columnspan=2, pady=20)

        tk.Button(root, text="Create Account", command=self.create_account).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(root, text="Deposit", command=self.deposit).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Withdraw", command=self.withdraw).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(root, text="Apply for Loan", command=self.apply_for_loan).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(root, text="View All Accounts", command=self.display_all_accounts).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="Logout", command=self.logout).grid(row=3, column=1, padx=10, pady=10)

    def create_account(self):
        name = simpledialog.askstring("Create Account", "Enter Account Holder Name:")
        initial_deposit = simpledialog.askfloat("Create Account", "Enter Initial Deposit:")
        if name and initial_deposit:
            result = self.system.create_account(name, initial_deposit)
            messagebox.showinfo("Success", result)

    def deposit(self):
        account_number = simpledialog.askinteger("Deposit", "Enter Account Number:")
        amount = simpledialog.askfloat("Deposit", "Enter Deposit Amount:")
        if account_number and amount:
            result = self.system.deposit(account_number, amount)
            messagebox.showinfo("Result", result)

    def withdraw(self):
        account_number = simpledialog.askinteger("Withdraw", "Enter Account Number:")
        amount = simpledialog.askfloat("Withdraw", "Enter Withdraw Amount:")
        if account_number and amount:
            result = self.system.withdraw(account_number, amount)
            messagebox.showinfo("Result", result)

    def apply_for_loan(self):
        name = simpledialog.askstring("Loan Application", "Enter Borrower Name:")
        loan_amount = simpledialog.askfloat("Loan Application", "Enter Loan Amount:")
        interest_rate = simpledialog.askfloat("Loan Application", "Enter Interest Rate:")
        duration = simpledialog.askinteger("Loan Application", "Enter Duration (in years):")
        if name and loan_amount and interest_rate and duration:
            result = self.system.apply_for_loan(name, loan_amount, interest_rate, duration)
            messagebox.showinfo("Loan Approved", result)

    def display_all_accounts(self):
        result = self.system.display_all_accounts()
        messagebox.showinfo("Accounts", result if result else "No accounts available.")

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

    tk.Label(root, text="Welcome to Banking Management System", font=("Helvetica", 16, "bold")).pack(pady=20)

    tk.Button(root, text="Login as Admin", command=lambda: load_admin(root, system), width=20).pack(pady=10)
    tk.Button(root, text="Login as Customer", command=lambda: load_customer(root, system), width=20).pack(pady=10)

    root.mainloop()


def load_admin(root, system):
    root.destroy()
    root = tk.Tk()
    AdminPortal(root, system)


def load_customer(root, system):
    root.destroy()
    root = tk.Tk()
    CustomerPortal(root, system)


if __name__ == "__main__":
    main()
