"""Lazy iterator chain"""


class MyChain:
    """
    Make an iterator that returns elements from the first iterable until it is
    exhausted, then proceeds to the next iterable, until all of the iterables
    are exhausted. If element is not iterated returns just this element
    """
    def __init__(self, *args):
        self.args = args
        self.index_x = 0
        self.index_y = 0

    def __next__(self):
        try:
            _ = self.args[self.index_x]
        except IndexError as err:
            raise StopIteration from err

        try:
            item = self.args[self.index_x][self.index_y]
        except TypeError:
            item = self.args[self.index_x]
            self.index_x += 1
        else:
            try:
                _ = self.args[self.index_x][self.index_y + 1]
            except IndexError:
                self.index_x += 1
                self.index_y = 0
            else:
                self.index_y += 1

        return item

    def __iter__(self):
        return self


zipped = MyChain(888, ['a', 'b', 'c', 'sdfsdf'], '£$%_', 5, 6, ['efggg', 9, 8])

for items in zipped:
    print(items)
