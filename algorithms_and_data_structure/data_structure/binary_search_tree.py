"""
Binary Search Tree:
    insert - добавить элемент,
    lookup - найти элемент по значению и вернуть ссылку на него (узел),
    delete - удалить элемент по значению),
"""


class IsNum:
    """
    Validator for node value. Should be int or float
    """
    def __init__(self):
        self.name = ''

    def __set__(self, instance, value):
        if isinstance(value, (float, int)):
            instance.__dict__[self.name] = value
        else:
            raise TypeError(
                print("Value should be int or float")
            )

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class Node:
    """
    Simple class to store value of current node and link to the next node
    """
    _value = IsNum()

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def get_value(self):
        """
        Gets value of the current node
        :return: int
        """
        if self._value or self._value == 0:
            return self._value
        return None

    def set_value(self, value):
        """
        Sets the value of current node
        :param value: int
        """
        self._value = value

    value = property(get_value, set_value)

    def get_left(self):
        """
        Gets the next left node
        :return: Node
        """
        if self._left:
            return self._left
        return None

    def set_left(self, value):
        """
        Sets the next left node
        :param value: int
        """
        self._left = value

    left = property(get_left, set_left)

    def get_right(self):
        """
        Gets the next right node
        :return: Node
        """
        if self._right:
            return self._right
        return None

    def set_right(self, value):
        """
        Sets the next right node
        :param value: int
        """
        self._right = value

    right = property(get_right, set_right)


class BinarySearchTree:
    """
    Class implements linked list structure
    """
    value = IsNum()

    def __init__(self, value=None):
        if value or value == 0:
            self.length = 1
            self._head = Node(value)
        else:
            self.length = 0
            self._head = None

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

    def search(self, value):
        """
        Goes through the tree and search the value of node.
        Returns set of the values (previous node, searched Node) or
        (previous node, None)
        :param value: int
        :return: Node, Node
        """
        current_node = self.head
        prev_node = None
        while current_node:
            if value == current_node.value:
                return prev_node, current_node
            if value > current_node.value:
                prev_node = current_node
                current_node = current_node.right
            else:
                prev_node = current_node
                current_node = current_node.left
        return prev_node, current_node

    def lookup(self, value):
        """
        Lookups the tree for a value. Returns node or None
        :param value: int
        :return: Node or None
        """
        if self.head is None:
            return None
        _, node = self.search(value)
        if node:
            return node
        return None

    def insert(self, new_value):
        """
        Inserts into the tree new node with value. Goes through the tree and
        find the correct place for new node. Returns None if the node with the
        same value almost exists.
        :param new_value: int
        :return: True or None
        """
        if self.head is None:
            self.head = Node(new_value)
            self.length += 1
            return True
        node, _ = self.search(new_value)
        if not node:
            return None
        if new_value == node.value:
            return None
        if new_value > node.value:
            node.right = Node(new_value)
        else:
            node.left = Node(new_value)
        self.length += 1
        return True

    def delete(self, del_value):
        """
        Deletes the node from the tree with the specified value. If no node
        with this value returns None
        :param del_value: int
        :return: None or True
        """
        if self.head is None:
            return None
        prev_node, del_node = self.search(del_value)
        if not del_node:
            return None
        left_child = del_node.left or None
        right_child = del_node.right or None
        if left_child:
            print(f'Left child of deleting node {del_value}: '
                  f'{left_child.value}')
        if right_child:
            print(f'Right child of deleting node {del_value}: '
                  f'{right_child.value}')
        if left_child:
            new_node = left_child
            if not new_node.right:
                new_node.right = right_child
            if prev_node:
                prev_node.left = new_node
            else:
                self.head = new_node
        else:
            if right_child.value > prev_node.value:
                prev_node.right = right_child
            else:
                prev_node.left = right_child
        self.length -= 1
        return True

    def show(self):
        """
        Prints the nodes of the tree and its children
        :return:
        """
        def get_children(node_):
            """
            Returns the list of the all children (left and right) nodes or None
            :param node_:
            :return:
            """
            children_ = []
            if node_.left:
                children_.append(node_.left)
                print(f'\t{node_.left.value}')
            if node_.right:
                children_.append(node_.right)
                print(f'\t{node_.right.value}')
            if children_:
                return children_
            print(f'\t{None}')
            return None

        print(f'{self.head.value}: ')
        children = get_children(self.head)

        while children:
            level = []
            for child in children:
                if isinstance(child, Node):
                    print(f'{child.value}: ')
                new_children = (get_children(child))
                if new_children:
                    level += new_children
            children = level

    def __len__(self):
        return self.length


if __name__ == '__main__':
    tree = BinarySearchTree(100)
    tree.insert(125)
    tree.insert(99)
    tree.insert(455)
    tree.insert(2)
    tree.insert(1)
    tree.insert(67)
    tree.show()
    print('length is ', len(tree))
    tree.delete(2)
    tree.show()
    tree.delete(99)
    tree.show()
    tree.delete(1)
    tree.show()
    tree.delete(444)
    # print('length is ', len(tree))
    tree.delete(100)
    tree.show()
