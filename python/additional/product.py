"""Lazy iterator zip"""
import itertools


class MyProduct:
    """
    Make a cartesian product of two inputted lists
    """
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        self.index_1 = 0
        self.index_2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            _ = self.arr2[self.index_2]
        except IndexError as error:
            self.index_2 = 0
            self.index_1 += 1

            if self.index_1 == len(self.arr1):
                raise StopIteration from error

        item1 = self.arr1[self.index_1]
        item2 = self.arr2[self.index_2]

        self.index_2 += 1

        return item1, item2


if __name__ == '__main__':
    product_old = itertools.product('ABCD', 'xyz')
    product_ = MyProduct('ABCD', 'xyz')
    for prd_o, prd in zip(product_old, product_):
        print(f'{prd_o} --> {prd} == {prd_o == prd}')
