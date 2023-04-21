class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up object
        :param name: Account name
        """
        self.__name = name
        self.__balance = 0.00

    def deposit(self, amount: float) -> bool:
        """
        Function to increment account balance by specified amount
        :param amount: Amount to increment balance by
        :return: Boolean if transaction completed
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to decrement account balance by specified amount
        :param amount: Amount to decrement balance by
        :return: Boolean if transaction completed
        """
        if self.__balance > amount and amount > 0:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to provide account balance
        :return: Current balance
        """
        return self.__balance

    def get_name(self) -> str:
        """
        Function to provide account name
        :return: Account name
        """
        return self.__name
