# Banking Management System
---

A Python-based GUI application built using Tkinter that simulates a banking management system. The system features an **Admin Portal** for account creation and management and a **Customer Portal** for banking transactions, loan management, and transaction history.

## Features

### **Admin Portal**  
Admins can:
- Log in using a secure password (`admin123`).
- Create new accounts for customers with an initial deposit.
- Delete existing customer accounts.
- View a list of all customer accounts.

### **Customer Portal**  
Customers can:
- Log in using their **account number** (provided by the admin at the time of account creation).
- Perform transactions:
  - Deposit money.
  - Withdraw money.
- Apply for loans:
  - Specify the loan amount, interest rate, and duration.
  - View the total payable amount and loan details.
- View transaction history, including deposits and withdrawals.
- View loans they have applied for.

### **Loan Management**  
- Customers can apply for loans with specified terms.
- Admin can manage customer accounts, enabling loan eligibility.

## Requirements

- **Python 3.x**  
- **Tkinter** (pre-installed with most Python distributions)
- **CSV Module** (for database storage, included in Python)
- **pytest** (for testing)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Install dependencies**:
   Install `pytest` for running the test suite:
   ```bash
   pip install pytest
   ```

## Running the Application

1. **Start the Application**:
   Run the main Python script:
   ```bash
   python banking_gui.py
   ```

2. **Login Options**:
   - **Admin Login**:  
     Click "Login as Admin" and enter the password `admin123` to access the Admin Portal.  
   - **Customer Login**:  
     Click "Login as Customer" and enter a valid **account number** to access the Customer Portal.

3. **Features**:
   - Admin can create/delete accounts and view all accounts.
   - Customers can deposit, withdraw, view transaction history, apply for loans, and view applied loans.

## Running the Tests

To verify the system’s functionality, run the test suite.

1. **Run tests**:
   ```bash
   pytest test_banking_system.py
   ```

2. **Expected Output**:
   All tests should pass, producing output similar to:
   ```bash
   ============================== test session starts ==============================
   collected 20 items

   test_banking_system.py ....................                   [100%]

   =============================== 20 passed in 0.50s ==============================
   ```

## Project Structure

```
banking_system/
│
├── banking_gui.py         # Main GUI application
├── banking_management_system.py  # Core system logic (BankAccount, LoanAccount)
├── accounts.csv           # Database of customer accounts
├── loans.csv              # Database of customer loans
├── test_banking_system.py # Test cases for the system
├── README.md              # Project documentation
└── requirements.txt       # Dependencies for the project
```

## Description of Key Classes

### 1. **BankAccount Class**  
- **Purpose**: Handles basic bank account operations.  
- **Features**:
  - Deposits and withdrawals.
  - Stores and displays account holder details and balance.
  - Records transaction history.

### 2. **LoanAccount Class**  
- **Purpose**: Handles loan details and calculations.  
- **Features**:
  - Stores loan amount, interest rate, and duration.
  - Calculates the total payable amount.

### 3. **BankingManagementSystem Class**  
- **Purpose**: Manages all customer accounts and loans.  
- **Features**:
  - Create, delete, and fetch accounts.
  - Save and load account and loan data from CSV files.
  - Manage loans applied by customers.

## CSV Databases

- **accounts.csv**: Stores customer account data, including account holder name, account number, and balance.
- **loans.csv**: Stores customer loan data, including borrower name, loan ID, loan amount, interest rate, and duration.

## Future Enhancements

- Implement more detailed reporting (e.g., monthly statements).
- Add an interest calculation feature for savings accounts.
- Improve security by encrypting sensitive data.
- Add multi-user support with individual logins.

## Conclusion

The Banking Management System provides a user-friendly interface for managing customer accounts and loans. It is designed with modularity in mind, making it easy to extend and adapt to additional requirements.

---

