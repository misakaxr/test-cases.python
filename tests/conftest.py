import json
from pathlib import Path

import pytest
from models.account import Account

DATA_FILE = Path(__file__).parent / "fixtures" / "accounts.json"


@pytest.fixture
def account():
    """An account with a balance of 100"""
    return Account(100)


@pytest.fixture
def empty_account():
    """An account with a zero balance"""
    return Account()


@pytest.fixture
def make_account():
    """Factory fixture: build an account with any balance"""
    def _make(balance=0):
        return Account(balance)
    return _make


@pytest.fixture(scope="session")
def account_data():
    """Load test data from JSON once for the whole run"""
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)