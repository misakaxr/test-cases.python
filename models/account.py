class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""


class Account:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")
        self.balance -= amount

    def transfer(self, other, amount):
        if not isinstance(other, Account):
            raise TypeError("Destination must be an Account")
        self.withdraw(amount)
        other.deposit(amount)

    def apply_interest(self, rate):
        if rate < 0:
            raise ValueError("Rate cannot be negative")
        self.balance += self.balance * rate