# import pytest
# from banking_management_system import BankingManagementSystem, BankAccount, FixedDepositAccount, LoanAccount

# # Fixture to initialize the Banking Management System
# @pytest.fixture
# def bms():
#     return BankingManagementSystem()

# # Test Account Creation
# def test_create_account(bms):
#     assert bms.create_account("John Doe", 2000) == "Account created successfully! Account Number: 1001"
#     assert bms.create_account("Alice", 5000) == "Account created successfully! Account Number: 1002"

# # Test Account Creation - Invalid Data
# def test_create_account_invalid(bms):
#     # Test empty name
#     with pytest.raises(ValueError, match="Name must be a non-empty string."):
#         bms.create_account("", 1000)
    
#     # Test invalid deposit amount
#     with pytest.raises(ValueError, match="Initial deposit must be a positive number."):
#         bms.create_account("John", -500)
    
#     # Test non-numeric deposit
#     with pytest.raises(ValueError, match="Initial deposit must be a positive number."):
#         bms.create_account("John", "invalid")

# # Test Deposit
# def test_deposit(bms):
#     bms.create_account("John Doe", 2000)
#     assert bms.deposit(1001, 500) == "Successfully deposited: 500"
#     assert bms.deposit(9999, 300) == "Account not found."

# # Test Withdraw
# def test_withdraw(bms):
#     bms.create_account("John Doe", 2000)
#     assert bms.withdraw(1001, 200) == "Successfully withdrew: 200"
#     assert bms.withdraw(1001, 5000) == "Insufficient balance or invalid withdrawal amount."
#     assert bms.withdraw(9999, 200) == "Account not found."

# # Test Fixed Deposit Creation
# def test_fixed_deposit(bms):
#     result = bms.create_fixed_deposit("Alice", 10000, 5, 6.5)
#     assert "Maturity Amount" in result
#     assert "Duration: 5 years" in result
#     assert "Interest Rate: 6.5%" in result

# # Test Loan Application
# def test_apply_loan(bms):
#     result = bms.apply_for_loan("Charlie", 50000, 10, 2)
#     assert "Loan Account Number: 3001" in result
#     assert "Loan Amount: 50000" in result
#     assert "Interest Rate: 10%" in result
#     assert "Duration: 2 years" in result

# # Test Display All Accounts
# def test_display_all_accounts(bms):
#     bms.create_account("John Doe", 2000)
#     bms.create_account("Alice", 5000)
#     accounts = bms.display_all_accounts()
#     assert len(accounts) == 2
#     assert "Account Holder: John Doe" in accounts[0]
#     assert "Account Holder: Alice" in accounts[1]

import pytest
from banking_management_system import BankingManagementSystem, BankAccount, FixedDepositAccount, LoanAccount


# Test Cases for Banking Management System
@pytest.fixture
def bms():
    return BankingManagementSystem()


def test_create_account_valid(bms):
    assert bms.create_account("Alice", 1000) == "Account created successfully! Account Number: 1001"


def test_create_account_invalid_name(bms):
    with pytest.raises(ValueError, match="Name must be a non-empty string."):
        bms.create_account("", 1000)


def test_create_account_invalid_deposit(bms):
    with pytest.raises(ValueError, match="Initial deposit must be a positive number."):
        bms.create_account("Alice", -500)


def test_deposit_valid(bms):
    bms.create_account("Bob", 2000)
    assert bms.deposit(1001, 500) == "Successfully deposited: 500"


def test_deposit_invalid_account(bms):
    assert bms.deposit(9999, 500) == "Account not found."


def test_withdraw_valid(bms):
    bms.create_account("Charlie", 3000)
    assert bms.withdraw(1001, 1000) == "Successfully withdrew: 1000"


def test_withdraw_exceeding_balance(bms):
    bms.create_account("David", 1500)
    assert bms.withdraw(1001, 2000) == "Insufficient balance or invalid withdrawal amount."


def test_withdraw_invalid_account(bms):
    assert bms.withdraw(9999, 100) == "Account not found."


def test_display_all_accounts(bms):
    bms.create_account("Alice", 1000)
    bms.create_account("Bob", 2000)
    accounts = bms.display_all_accounts()
    assert len(accounts) == 2
    assert "Account Holder: Alice" in accounts[0]
    assert "Account Holder: Bob" in accounts[1]


# Test Cases for Fixed Deposit
def test_create_fixed_deposit_valid(bms):
    result = bms.create_fixed_deposit("Alice", 5000, 3, 5.5)
    assert "Maturity Amount" in result
    assert "Interest Rate: 5.5%" in result


def test_calculate_fixed_deposit_maturity_amount():
    fd = FixedDepositAccount("Bob", 2001, 10000, 2, 7.5)
    maturity_amount = fd.calculate_maturity_amount()
    assert maturity_amount == pytest.approx(11556.25, rel=1e-2)


def test_display_fixed_deposit_details():
    fd = FixedDepositAccount("Charlie", 2002, 15000, 4, 6.0)
    details = fd.display_fixed_deposit_details()
    assert "Account Holder: Charlie" in details
    assert "Duration: 4 years" in details
    assert "Interest Rate: 6.0%" in details


# Test Cases for Loan Account
def test_apply_for_loan_valid(bms):
    result = bms.apply_for_loan("Alice", 10000, 5.0, 2)
    assert "Loan Amount: 10000" in result
    assert "Interest Rate: 5.0%" in result


def test_calculate_loan_total_payable():
    loan = LoanAccount("David", 3001, 20000, 6.0, 3)
    total_payable = loan.calculate_total_payable()
    assert total_payable == pytest.approx(23819.2, rel=1e-2)


def test_display_loan_details():
    loan = LoanAccount("Emma", 3002, 15000, 4.5, 5)
    details = loan.display_loan_details()
    assert "Borrower Name: Emma" in details
    assert "Loan Amount: 15000" in details
    assert "Interest Rate: 4.5%" in details
    assert "Total Payable" in details


# Edge Cases and Miscellaneous
def test_negative_deposit(bms):
    bms.create_account("Alice", 1000)
    assert bms.deposit(1001, -200) == "Invalid deposit amount."


def test_zero_deposit(bms):
    bms.create_account("Alice", 1000)
    assert bms.deposit(1001, 0) == "Invalid deposit amount."


def test_zero_withdrawal(bms):
    bms.create_account("Alice", 1000)
    assert bms.withdraw(1001, 0) == "Insufficient balance or invalid withdrawal amount."


def test_empty_account_list(bms):
    accounts = bms.display_all_accounts()
    assert accounts == []


def test_apply_loan_invalid_amount(bms):
    with pytest.raises(ValueError):
        bms.apply_for_loan("Alice", -10000, 5.0, 2)
