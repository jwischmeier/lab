import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'

    def test_deposit(self):
        assert self.a1.deposit(-1.50) is False
        assert self.a1.get_balance() == 0.00

        assert self.a1.deposit(0.00) is False
        assert self.a1.get_balance() == 0.00

        assert self.a1.deposit(1.50) is True
        assert self.a1.get_balance() == 1.50

    def test_withdraw(self):
        assert self.a1.withdraw(-1.50) is False
        assert self.a1.get_balance() == 0.00

        assert self.a1.withdraw(0.00) is False
        assert self.a1.get_balance() == 0.00

        assert self.a1.withdraw(1.50) is False
        assert self.a1.get_balance() == 0.00

        assert self.a1.deposit(2.50) is True
        assert self.a1.withdraw(1.50) is True
        assert self.a1.get_balance() == 1.00

    def test_get_balance(self):
        assert self.a1.get_balance() == 0.00

    def test_get_name(self):
        assert self.a1.get_name() is 'John'