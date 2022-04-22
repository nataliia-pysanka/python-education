"""
Generator for arithmetic progression
"""
import time


class ArithmeticProgression:
    """
    Class-generator
    """
    def __str__(self):
        return f"Arithmetic progression with {self.num} numbers for base " \
               f"{self.base} with increment {self.inc}"

    def __init__(self, base=0, inc=1, num=100):
        self.base = base
        self.inc = inc
        self.num = num

    def __iter__(self):
        while self.num > 0:
            yield self.base
            self.base += self.inc
            self.num -= 1


if __name__ == '__main__':
    progression = ArithmeticProgression(1542, 543)

    for item in progression:
        print(item)
        time.sleep(0.05)
