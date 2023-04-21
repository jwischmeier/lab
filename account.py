class Account:
    def __init__(self, name):
        self.__name = name
        self.__balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.__balance > amount and amount > 0:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name
