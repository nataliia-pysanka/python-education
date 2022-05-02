"""
LinkedList:
    prepend - add item to the head of the list,
    append - add item to the tail of the list,
    lookup - find the first index of value,
    insert - insert an element at the specific index
            with elements shifted to the right,
    delete - delete the element by the index
"""


class Node:
    """
    Simple class to store value of current node and link to the next node
    """
    def __init__(self, value=None):
        self._value = value
        self._next_node = None

    def get_value(self):
        """
        Gets value of the current node
        :return: any
        """
        return self._value

    def set_value(self, value):
        """
        Sets the value of current node
        :param value: any
        """
        self._value = value

    value = property(get_value, set_value)

    def get_next_node(self):
        """
        Gets the link to the next node
        :return: Node or None
        """
        return self._next_node

    def set_next_node(self, node):
        """
        Sets the link to the next node
        :param node: Node
        """
        self._next_node = node

    next = property(get_next_node, set_next_node)


class LinkedList:
    """
    Class implements linked list structure
    """
    def __init__(self, value=None):
        if value:
            self.length = 1
            self._head = Node(value)
            self._head.next = Node()
        else:
            self.length = 0
            self._head = None
        self._tail = self._head

    @property
    def head_value(self):
        """
        Gets the value of head of the list
        :return: any
        """
        return self._head.value

    @property
    def tail_value(self):
        """
        Gets the value of tail of the list
        :return: any
        """
        return self._tail.value

    def get_head(self):
        """
        Gets the node of the head
        :return: Node or None
        """
        if not self._head:
            return None
        return self._head

    def set_head(self, node: Node):
        """
        Sets the node to the head
        :param node: Node
        """
        self._head = node

    head = property(get_head, set_head)

    def get_tail(self):
        """
        Gets the node of the tail
        :return: Node or None
        """
        if not self._tail:
            return None
        return self._tail

    def set_tail(self, node: Node):
        """
        Sets the node to the tail
        :param node: Node
        """
        self._tail = node

    tail = property(get_tail, set_tail)

    def create_first(self, value):
        """
        Create first node if the list is empty
        :param value:
        :return:
        """
        self.head = Node(value)
        self.head.next = Node()
        self.tail = self.head
        self.length += 1

    def append(self, value):
        """
        Adds the item to the tail of the list
        :param value: any
        """
        if self.head is None:
            self.create_first(value)
            return
        self.length += 1
        tail = self.tail.next
        tail.value = value
        tail.next = Node()
        self.tail = tail

    def prepend(self, value):
        """
        Adds the item to the head of the list
        :param value: any
        """
        if self.head is None:
            self.create_first(value)
            return
        self.length += 1
        node = self.head
        new_node = Node(value)
        new_node.next = node
        self.head = new_node

    def lookup(self, value):
        """
        Finds the first index of the value
        :param value: any
        :return: int or None
        """
        index = 0
        for item in self:
            if item.value == value:
                return index
            index += 1
        return None

    def __getitem__(self, index):
        """
        Finds the node with index
        :param index: int
        :return: Node or None
        """
        if index > len(self) or index < 0 or len(self) == 0:
            return None
        current_index = 0
        for item in self:
            if index == current_index:
                return item.value
            current_index += 1
        return None

    def __setitem__(self, key, value):
        """
        Sets the value of node with index
        :param index: int
        :return: Node or None
        """
        if key > len(self) or key < 0:
            return None
        current_index = 0
        for item in self:
            if key == current_index:
                item.value = value
                return True
            current_index += 1
        return None

    def __iter__(self):
        return ListIter(self)

    def show(self):
        """
        Prints the whole list with indexes
        """
        index = 0
        for item in self:
            print(f'{index} - {item.value}')
            index += 1
        print()

    def __len__(self):
        return self.length

    def insert(self, ins_index, ins_value):
        """
        Inserts an element at the specific index with elements
        shifted to the right. If the index is bigger then length of the list
        then new item appends to the tail of the list
        :param ins_index: int
        :param ins_value: any
        """
        if ins_index > len(self):
            self.append(ins_value)
            return
        if len(self) == 0:
            self.create_first(ins_value)
            return
        if ins_index == 0:
            self.prepend(ins_value)
            return
        self.length += 1
        index = 1
        old_node = self.head
        for _ in self:
            if index == ins_index:
                new_node = Node(ins_value)
                new_node.next = old_node.next
                old_node.next = new_node
                break
            old_node = old_node.next
            index += 1

    def delete(self, del_index):
        """
        Deletes the element by the index. Returns None if index doesn't exist
        :param del_index:
        """
        if del_index > len(self):
            return None
        if len(self) == 0:
            return None
        if del_index == 0:
            self.length -= 1
            self.head = self.head.next
            return None
        self.length -= 1
        index = 1
        old_node = self.head
        for _ in self:
            if index == del_index:
                del_node = old_node.next
                old_node.next = del_node.next
                self.tail = old_node
                break
            old_node = old_node.next
            index += 1
        return None


class ListIter:
    """
    Class-iterator for linked list
    """
    def __init__(self, lst):
        self.item = lst.head

    def __next__(self):
        if self.item.value is None:
            raise StopIteration
        value = self.item
        self.item = self.item.next
        return value

    def __iter__(self):
        return self


if __name__ == '__main__':
    my_list = LinkedList("First node")
    my_list.prepend("zero node")
    my_list.append("Second node")
    my_list.append("Third node")
    my_list.append("Fourth node")
    my_list.append("Fifth node")
    my_list.append("Sixth node")
    my_list.show()
    print(f'The head is "{my_list.head_value}"')
    print(f'The tail is "{my_list.tail_value}"')

    print(len(my_list))
    my_list.delete(len(my_list)-1)
    print(len(my_list))
    my_list.show()
    print(f'The head is "{my_list.head_value}"')
    print(f'The tail is "{my_list.tail_value}"')

    FIND_ITEM = "Fifth node"
    print(f'The index of "{FIND_ITEM}" is {my_list.lookup(FIND_ITEM)}')
    print()
    my_list.insert(55, 'new node')
    my_list.show()
    my_list.delete(88)
    my_list.show()
    print(f'The head is "{my_list.head_value}"')
    print(f'The tail is "{my_list.tail_value}"')
    print()
    print(f'this is 6th item {my_list[6]}')
    my_list[6] = 'hello'
    my_list.show()
