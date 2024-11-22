
# Banking Management System

A simple banking management system built using Python and Tkinter for GUI. This system allows users to create accounts, deposit and withdraw money, apply for loans, and view account details. It also features an **Admin Portal** for managing accounts and a **Customer Portal** for banking transactions.

## Features
- **Account Management:**
  - Create new accounts with an initial deposit.
  - Deposit money into accounts.
  - Withdraw money from accounts.
  - Display account details.

- **Fixed Deposit Accounts:**
  - Create fixed deposit accounts with a specified interest rate and duration.
  - Calculate maturity amount after the specified duration.

- **Loan Management:**
  - Apply for a loan.
  - Calculate the total payable amount for the loan based on interest rate and duration.

- **Admin Portal:**
  - Admins can create and delete accounts.
  - Admins can view all accounts in the system.

- **Customer Portal:**
  - Customers can manage their accounts (deposit, withdraw, and apply for loans).

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)
- pytest (for running tests)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Install dependencies**:
   If you don't have `pytest` installed, you can install it using pip:
   ```bash
   pip install pytest
   ```

## Running the Application

1. **Run the GUI application**:
   In your terminal, navigate to the project directory and run the main Python script:
   ```bash
   python banking_system_gui.py
   ```
   This will open a GUI window where you can log in as an **Admin** or a **Customer** and perform the following actions:
   - **Admin**: Create, delete, and view accounts.
   - **Customer**: Create accounts, deposit, withdraw, and apply for loans.

2. **Login Credentials**:
   - **Admin Login**: 
     - Password: `admin123`
   - **Customer Login**: 
     - You can create new accounts and manage them.

## Running the Tests

To ensure everything is working as expected, you can run the provided test suite with `pytest`.

1. **Run tests using pytest**:
   Navigate to the project directory and run the tests:
   ```bash
   pytest test_banking_management_system.py
   ```

2. **Expected Output**:
   If all tests pass, you should see something like:
   ```bash
   ============================== test session starts ==============================
   collected 20 items

   test_banking_management_system.py ....................                   [100%]

   =============================== 20 passed in 0.50s ==============================
   ```

## Project Structure

```
banking_system/
│
├── banking_system_gui.py         # Main GUI application
├── banking_management_system.py  # Core system logic (BankAccount, FixedDepositAccount, LoanAccount)
├── test_banking_management_system.py  # Test cases for the system
├── README.md                     # Project documentation
└── requirements.txt               # (Optional) List of dependencies
```

## Description of Classes and Methods

### 1. **BankAccount Class**
- Handles creation, deposit, withdrawal, and account details for a standard bank account.

### 2. **FixedDepositAccount Class** (Inherits `BankAccount`)
- Manages fixed deposit accounts with interest rates and durations.
- **Methods**:
  - `calculate_maturity_amount`: Calculates maturity amount after the specified duration.
  - `display_fixed_deposit_details`: Displays account details along with maturity amount.

### 3. **LoanAccount Class**
- Manages loan accounts with loan amounts, interest rates, and durations.
- **Methods**:
  - `calculate_total_payable`: Calculates the total amount to be paid for the loan after interest.
  - `display_loan_details`: Displays loan account details.

### 4. **BankingManagementSystem Class**
- Manages all accounts, fixed deposits, and loan accounts.
- **Methods**:
  - `create_account`: Creates a new bank account.
  - `deposit`: Deposits money into an account.
  - `withdraw`: Withdraws money from an account.
  - `create_fixed_deposit`: Creates a fixed deposit account.
  - `apply_for_loan`: Applies for a new loan.
  - `display_all_accounts`: Displays all bank accounts.

## Conclusion

This Banking Management System provides a simple and intuitive interface for both customers and admins to manage bank accounts, fixed deposits, and loans. It can be extended further with additional features like transaction history, reports, and more complex account management functionalities.

---
