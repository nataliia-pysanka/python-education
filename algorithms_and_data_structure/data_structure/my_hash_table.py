"""
HashTable:
    insert - добавить элемент с ключом (индекс = хеш_функция(ключ)),
    lookup - получить значение по ключу, delete - удалить значение по ключу
"""
import datetime
from my_linked_list import LinkedList


class MySet:
    """
    Class for restoring couple of items: key and value
    """
    def __init__(self, set_key, set_value):
        self._key = set_key
        self._value = set_value

    def get_key(self):
        """
        Returns the key of the couple
        """
        return self._key

    def set_key(self, new_key):
        """
        Changes the key in the couple
        """
        self._key = new_key

    key = property(get_key, set_key)

    def get_value(self):
        """
        Returns the value of the couple
        """
        return self._value

    def set_value(self, new_value):
        """
        Changes the value in the couple
        """
        self._value = new_value

    value = property(get_value, set_value)

    def __str__(self):
        return f'{self.key}: {self.value}'


class MyHashTable:
    """
    Class for hash-table
    """
    COUNT = 30

    def __init__(self):
        self._storage = LinkedList()
        for _ in range(MyHashTable.COUNT):
            self._storage.append(LinkedList())
        self._hash = None
        self._key = None

    def get_key(self):
        """
        Returns value of current key
        """
        return self._key

    def set_key(self, new_value):
        """
        Sets value of current key
        """
        self._key = new_value

    key = property(get_key, set_key)

    def get_hash(self):
        """
        Returns value of current hash
        """
        return self._hash

    def set_hash(self, new_value):
        """
        Sets value of current hash
        """
        self._hash = new_value

    hash = property(get_hash, set_hash)

    def calc_hash(self, new_value=None):
        """
        Calculates hash-value
        :param new_value: str
        :return: int
        """
        if not new_value:
            new_value = self.key
        hash_ = 0
        for char in new_value:
            hash_ += ord(char)
        return hash_ % MyHashTable.COUNT

    def get_storage(self):
        """
        Returns linked list by current hash
        """
        lst = self._storage[self.hash]
        if lst:
            return lst
        return None

    def set_storage(self, new_value):
        """
        Adds new node to the linked list by its hash
        :param new_value: any
        """
        self._storage[self.hash].append(new_value)

    storage = property(get_storage, set_storage)

    def __len__(self):
        length = 0
        for index in range(MyHashTable.COUNT):
            self.hash = index
            if not self.storage:
                continue
            length += len(self.storage)
        return length

    def lookup(self, look_key):
        """
        Finds the item by key in the table
        :param look_key: any non-changeable
        :return: any or None
        """
        self.key = look_key
        self.hash = self.calc_hash(look_key)
        temp = self.storage
        if not temp:
            return None
        for tmp_item in temp:
            if tmp_item.value.key == self.key:
                return tmp_item.value.value
        return None

    def insert(self, ins_key, ins_value):
        """
        Inserts item into table
        :param ins_key: any non-changeable
        :param ins_value: any
        """
        self.key = ins_key
        self.hash = self.calc_hash(ins_key)
        node = MySet(ins_key, ins_value)
        self.storage = node

    def delete(self, del_key):
        """
        Deletes item from table by its key
        :param del_key: any non-changeable
        :return: None or True
        """
        self.key = del_key
        self.hash = self.calc_hash(del_key)
        temp = self.storage
        if not temp:
            return None
        index = 0
        for tmp_item in temp:
            if tmp_item.value.key == self.key:
                temp.delete(index)
                return True
            index += 1
        return None

    def show(self):
        """
        Prints all the items of the hash-table
        """
        for key, value in self.get_items():
            print(f'{key}: {value}')

    def get_keys(self):
        """
        Return all the keys of the hash-table
        :return: list
        """
        keys = []
        for self.hash in range(MyHashTable.COUNT):
            lst = self.storage
            if lst:
                keys += [item_.value.key for item_ in lst]
        return keys

    def get_values(self):
        """
        Returns all values of the hash-table
        :return: list
        """
        values = []
        for self.hash in range(MyHashTable.COUNT):
            lst = self.storage
            if lst:
                values += [item_.value.value for item_ in lst]
        return values

    def get_items(self):
        """
        Returns all items of hash-table like a set
        :return: set
        """
        items = []
        for self.hash in range(MyHashTable.COUNT):
            lst = self.storage
            if lst:
                items += [(item_.value.key, item_.value.value)
                          for item_ in lst]
        return items

    def __getitem__(self, key_):
        self.key = key_
        self.hash = self.calc_hash(key_)
        temp = self.storage
        if not temp:
            return None
        for tmp_item in temp:
            if tmp_item.value.key == key_:
                return tmp_item
        return None


def generate_item():
    """
    Generates unique items
    :return: set
    """
    gen_key = str(datetime.datetime.now())
    gen_item = f'this is item of {gen_key}'
    return gen_key, gen_item


if __name__ == '__main__':
    table_100 = MyHashTable()
    for i in range(10):
        item = generate_item()
        table_100.insert(str(i), item[1])

    table_100.show()
    print()
    print(table_100['2'].value)
