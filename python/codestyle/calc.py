"""
Classic calculator
"""


class Calculator:
    """
    A class to calculate some numbers
    """
    def __init__(self, *args):
        self.args = args

    def add(self):
        """
        Adds all arguments to each other
        :return: int, float
        """
        res = 0
        for arg in self.args:
            res += arg
        return res

    def sub(self):
        """
        Subtracts from first argument others
        :return: int, float
        """
        res = self.args[0]
        for index in range(1, len(self.args)):
            res -= self.args[index]
        return res

    def mul(self):
        """
        Multiples all arguments
        :return: int, float
        """
        res = 1
        for arg in self.args:
            res *= arg
        return res

    def div(self):
        """
        Divides first argument to others
        :return: float
        """
        res = self.args[0]
        for index in range(1, len(self.args)):
            res /= self.args[index]
        return res
