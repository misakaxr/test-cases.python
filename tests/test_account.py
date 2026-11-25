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


def test_transfer_moves_money(account, make_account):
    dest = make_account(20)
    account.transfer(dest, 30)
    assert account.balance == 70
    assert dest.balance == 50



def test_apply_interest_increases_balance(account):
    account.apply_interest(0.05)
    assert account.balance == 105


def test_apply_interest_negative_rate_raises_error(account):
    with pytest.raises(ValueError):
        account.apply_interest(-0.1)


def test_transfer_to_non_account_raises_type_error(account):
    with pytest.raises(TypeError):
        account.transfer("not an account", 10)


def test_transfer_insufficient_funds_raises_error(make_account):
    with pytest.raises(InsufficientFundsError):
        make_account(10).transfer(make_account(0), 50)