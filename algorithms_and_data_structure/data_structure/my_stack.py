"""
Stack:
    push - добавить элемент в стек,
    pop - изъять последний элемент,
    peek - получить значение крайнего элемента стека
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


class Stack:
    """
    Class implements stack structure
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
    def peek(self):
        """
        Gets the value of head of the queue
        :return: any
        """
        if self.head:
            return self.head.value
        return None

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
        Creates first node if the queue is empty
        :param value:
        :return:
        """
        self.head = Node(value)
        self.head.next = Node()
        self.tail = self.head
        self.length += 1

    def __iter__(self):
        return ListIter(self)

    def show(self):
        """
        Prints the whole queue with indexes
        """
        index = 0
        for item in self:
            print(f'{index} - {item}')
            index += 1
        print()

    def __len__(self):
        return self.length

    def push(self, value):
        """
        Adds the node to the stack
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

    def pop(self):
        """
        Returns the node from the stack
        :return:
        """
        if len(self) == 0:
            return None
        self.length -= 1
        node = self.head
        self.head = self.head.next
        return node.value


class ListIter:
    """
    Class-iterator for linked list
    """
    def __init__(self, lst):
        self.item = lst.head

    def __next__(self):
        if self.item.value is None:
            raise StopIteration
        value = self.item.value
        self.item = self.item.next
        return value

    def __iter__(self):
        return self


if __name__ == '__main__':
    my_list = Stack("zero node")
    print(my_list.peek)
    my_list.push("zero node")
    my_list.push("Second node")
    my_list.push("Third node")
    my_list.push("Fourth node")
    my_list.push("Fifth node")
    my_list.push("Sixth node")
    print(my_list.peek)
    my_list.show()

    for i in range(len(my_list)):
        print(my_list.pop())
    my_list.show()
    print(my_list.peek)
