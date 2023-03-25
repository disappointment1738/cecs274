import SLLQueue
from Interfaces import Tree


class BinaryTree(Tree):
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val

        def set_key(self, x):
            self.k = x

        def set_val(self, v):
            self.v = v

        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left

        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right

        def __str__(self):
            return f"({self.k}, {self.v})"

    def __init__(self):
        self.r = None

    def depth(self, u: Node) -> int:
        # todo
        pass

    def height(self) -> int:
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        # todo
        pass

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        # todo
        pass

    def bf_order(self):
        # todo
        pass

    def in_order(self) -> list:
        return self._in_order(self.r)

    def _in_order(self, u: Node) -> list:
        # todo
        pass

    def post_order(self) -> list:
        return self._post_order(self.r)

    def _post_order(self, u: Node):
        # todo
        pass

    def pre_order(self) -> list:
        return self._pre_order(self.r)

    def _pre_order(self, u: Node):
        # todo
        pass

    def __str__(self):
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)