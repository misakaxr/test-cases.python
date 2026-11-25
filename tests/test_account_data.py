import json
from pathlib import Path

import pytest
from models.account import Account

DATA = json.loads(
    (Path(__file__).parent / "fixtures" / "accounts.json").read_text(encoding="utf-8")
)


def test_accounts_built_from_json(account_data):
    """Fixture style: build objects from the loaded data"""
    accounts = [Account(item["balance"]) for item in account_data["accounts"]]
    assert [a.balance for a in accounts] == [100, 500, 0]


@pytest.mark.parametrize("case", DATA["deposit_cases"])
def test_deposit_cases_from_json(case):
    """Parametrize style: one test run per JSON entry"""
    acc = Account(case["start"])
    acc.deposit(case["amount"])
    assert acc.balance == case["expected"]


@pytest.mark.parametrize("amount", DATA["invalid_amounts"])
def test_invalid_deposits_from_json(amount):
    with pytest.raises(ValueError):
        Account(100).deposit(amount)