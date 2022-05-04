"""
Quick sort algorithm
"""


def partinition(lst_, low, high):
    """
    Makes partitioning of the list
    :param lst_: list
    :param low: min index
    :param high: max index
    :return: int
    """
    pivot = lst_[high]
    pointer = low - 1
    for index in range(low, high):
        item = lst_[index]
        if item <= pivot:
            pointer += 1
            lst_[pointer], lst_[index] = lst_[index], lst_[pointer]
    lst_[pointer + 1], lst_[high] = lst_[high], lst_[pointer + 1]
    return pointer + 1


def quick_sort(lst):
    """
    Makes quick sort by iterating
    :param lst: list
    :return: list
    """
    stack = [(0, len(lst) - 1)]
    while stack:
        low, high = stack.pop()
        part_index = partinition(lst, low, high)
        if part_index - 1 > low:
            stack.append((low, part_index - 1))
        if part_index + 1 < high:
            stack.append((part_index + 1, high))
    return lst
