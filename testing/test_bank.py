import pytest
from bank import BankAccount

def test_default_balance():
    account = BankAccount("Bob")
    assert account.balance == 0.0
    assert account.owner == "Bob"

def test_single_deposit():
    account = BankAccount("Bob", balance=0.0)
    account.deposit(100.0)
    assert account.balance == 100.0

def test_multiple_deposit():
    account = BankAccount("Bob", balance=0.0)
    account.deposit(100.0)
    account.deposit(100.0)
    assert account.balance == 200.0

def test_withdrawal_reduces_balance(funded_account):
    funded_account.withdraw(200.0)
    assert funded_account.balance == 800.0

def test_withdraw_insufficient_funds(funded_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        funded_account.withdraw(6000.0)

def test_deposit_negative(funded_account):
    with pytest.raises(ValueError, match="Amount must be positive"):
        funded_account.deposit(-50.0)

def test_account_repr():
    account = BankAccount("Charlie", 150.5)
    assert repr(account) == "BankAccount(owner='Charlie', balance=150.5)"