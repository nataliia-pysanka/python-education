"""Lazy iterator zip"""


class MyZip:
    """
    Make an iterator that aggregates elements from each of the iterables.
    If the iterables are of uneven length, missing values are filled-in with
    fillvalue. Iteration continues until the longest iterable is exhausted
    """
    def __init__(self, arr1, arr2, fillvalue='*'):
        self.arr1 = arr1
        self.arr2 = arr2
        self.fillvalue = fillvalue
        self.index = 0
        self.length = len(arr1) if len(arr1) > len(arr2) else len(arr2)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.length:
            raise StopIteration

        try:
            item1 = self.arr1[self.index]
        except IndexError:
            item1 = self.fillvalue

        try:
            item2 = self.arr2[self.index]
        except IndexError:
            item2 = self.fillvalue
        self.index += 1

        return item1, item2


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    zipped = MyZip(numbers, letters)

    for a, b in zipped:
        print(a, b)
