"""
Graph (ненаправленный, ребра без весов):
    insert - добавить узел и связи с другими узлами по ссылкам,
    lookup - найти узел по значению и вернуть ссылку на него,
    delete - удалить узел по ссылке и связи с другими узлами
"""
from my_hash_table import MyHashTable
from my_linked_list import LinkedList


class ListOfEdges:
    """
        Simple class to store value of current node and links to the
        neighbors nodes
    """
    def __init__(self, *edges):
        self._edges = LinkedList()
        if edges:
            for edge in edges:
                self._edges.append(edge)

    def get_edges(self):
        """
        Gets edges for current node
        :return: LinkedList
        """
        return self._edges

    def set_edges(self, edge_):
        """
        Appends new edge to the list of edges
        :param edge_: any
        """
        self._edges.append(edge_)

    def del_edges(self):
        """
        Deletes the whole list of the edges
        """
        self._edges = LinkedList()

    edges = property(get_edges, set_edges)

    def __str__(self):
        edges = ''
        for edge in self.edges:
            edges += edge.value + ' '
        return edges


class MyGraph:
    """
    Class for graph
    """
    def __init__(self):
        self._graph = MyHashTable()

    def insert(self, node: str, *edges):
        """
        Inserts node with edges to the graph
        :param node: str
        :param edges: str
        :return:
        """
        if self.lookup(node):
            return None
        list_of_edges = ListOfEdges(*edges)
        self._graph.insert(node, list_of_edges)
        return True

    def show(self):
        """
        Prints the node with its edges
        :return:
        """
        for key, value in self._graph.get_items():
            print(f'{key}: {value}')

    def lookup(self, node_):
        """
        Finds the specific node
        :param node_: str
        :return: Node
        """
        for key, value in self._graph.get_items():
            if key == node_:
                print(f'{key}: {value}')
                return self._graph[key]
        return None

    def delete(self, node_):
        """
        Deletes the node from the graph
        :param node_: str
        :return:
        """
        for key in self._graph.get_keys():
            if key == node_:
                print(f'Node {node_} deleted')
                self._graph.delete(node_)
                return True
        return None

    def __len__(self):
        return len(self._graph)


if __name__ == '__main__':
    graph = MyGraph()
    graph.insert('A', 'B', 'C', 'K')
    graph.insert('B', 'A', 'D', 'E', 'F')
    graph.insert('C', 'A')
    graph.insert('D', 'B')
    graph.insert('E', 'B', 'A')
    graph.insert('F', 'B', 'C', 'K')
    graph.insert('K', 'A')
    graph.insert('L', 'K')
    graph.show()
    print()
    print(graph.lookup('E'))
    graph.delete('E')
    graph.show()
    print(graph.lookup('E'))
    graph.delete('E')
    graph.show()
