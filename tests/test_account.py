import pytest
from models.account import Account, InsufficientFundsError


def test_new_account_default_balance_is_zero():
    assert Account().balance == 0


def test_new_account_with_starting_balance():
    assert Account(100).balance == 100


def test_negative_starting_balance_raises_error():
    with pytest.raises(ValueError):
        Account(-10)


def test_deposit_increases_balance():
    acc = Account(100)
    acc.deposit(50)
    assert acc.balance == 150


def test_deposit_negative_amount_raises_error():
    acc = Account(100)
    with pytest.raises(ValueError):
        acc.deposit(-5)


def test_withdraw_decreases_balance():
    acc = Account(100)
    acc.withdraw(30)
    assert acc.balance == 70


def test_withdraw_more_than_balance_raises_error():
    acc = Account(50)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(100)


def test_withdraw_zero_raises_error():
    acc = Account(50)
    with pytest.raises(ValueError):
        acc.withdraw(0)