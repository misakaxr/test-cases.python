from behave import given, when, then
from models.account import Account, InsufficientFundsError


@given("an account with a balance of {balance:d}")
def step_given_account(context, balance):
    context.account = Account(balance)
    context.error = None


@when("I deposit {amount:d}")
def step_deposit(context, amount):
    context.account.deposit(amount)


@when("I withdraw {amount:d}")
def step_withdraw(context, amount):
    context.account.withdraw(amount)


@when("I try to withdraw {amount:d}")
def step_try_withdraw(context, amount):
    try:
        context.account.withdraw(amount)
    except InsufficientFundsError as e:
        context.error = e


@then("the balance should be {expected:d}")
def step_check_balance(context, expected):
    assert context.account.balance == expected


@then("I should see an insufficient funds error")
def step_check_error(context):
    assert isinstance(context.error, InsufficientFundsError)