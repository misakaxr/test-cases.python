import unittest
from models.account import Account, InsufficientFundsError


class TestAccount(unittest.TestCase):
    """Test cases for the Account model"""

    def setUp(self):
        self.acc = Account(100)

    def test_default_balance(self):
        """It should start with a zero balance"""
        self.assertEqual(Account().balance, 0)

    def test_negative_starting_balance(self):
        """It should reject a negative starting balance"""
        with self.assertRaises(ValueError):
            Account(-10)

    def test_deposit(self):
        """It should increase the balance on deposit"""
        self.acc.deposit(50)
        self.assertEqual(self.acc.balance, 150)

    def test_deposit_negative(self):
        """It should reject a negative deposit"""
        with self.assertRaises(ValueError):
            self.acc.deposit(-5)

    def test_withdraw(self):
        """It should decrease the balance on withdrawal"""
        self.acc.withdraw(30)
        self.assertEqual(self.acc.balance, 70)

    def test_withdraw_too_much(self):
        """It should raise an error when funds are insufficient"""
        with self.assertRaises(InsufficientFundsError):
            self.acc.withdraw(500)

    def test_withdraw_zero(self):
        """It should reject a zero withdrawal"""
        with self.assertRaises(ValueError):
            self.acc.withdraw(0)