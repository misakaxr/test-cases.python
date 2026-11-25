import factory
from models.account import Account


class AccountFactory(factory.Factory):
    """Builds Account objects with random starting balances"""

    class Meta:
        model = Account

    balance = factory.Faker("pyint", min_value=1, max_value=10_000)