import pytest
from factory.random import reseed_random
from faker import Faker

from models.account import InsufficientFundsError
from tests.factories import AccountFactory

fake = Faker()

# Optional: makes the "random" values repeat on every run, so failures are reproducible
reseed_random(1234)
Faker.seed(1234)


def test_factory_builds_valid_account():
    acc = AccountFactory()
    assert acc.balance > 0


def test_create_batch():
    accounts = AccountFactory.create_batch(5)
    assert len(accounts) == 5
    assert all(a.balance > 0 for a in accounts)


def test_deposit_random_amount():
    acc = AccountFactory()
    start = acc.balance
    amount = fake.pyint(min_value=1, max_value=500)
    acc.deposit(amount)
    assert acc.balance == start + amount


def test_withdraw_more_than_balance_raises_error():
    acc = AccountFactory(balance=100)          # override the random value
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(acc.balance + 1)


def test_transfer_keeps_total_money_the_same():
    src = AccountFactory(balance=500)
    dst = AccountFactory(balance=0)
    amount = fake.pyint(min_value=1, max_value=500)
    src.transfer(dst, amount)
    assert src.balance + dst.balance == 500
    assert dst.balance == amount