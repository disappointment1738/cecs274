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
        # check the precondition: is u nil?
        if u is None:
            return -1
        # keep track of edges in the path from node u to the root
        d = 0
        current_node = u
        # move up the tree until u is the root
        while current_node != self.r:
            current_node = current_node.parent
            d += 1 # increment edge by 1
        return d

    def height(self) -> int:
        return self._height(self.r)

    def _height(self, u: Node) -> int:
        # base case: is u nil?
        if u is None:
            return -1
        # recursive (reduction) step
        return 1 + max(self._height(u.left), self._height(u.right))

    def size(self) -> int:
        return self._size(self.r)

    def _size(self, u: Node) -> int:
        # base case: is u nil?
        if u is None:
            return 0
        # recursive (reduction) step
        return 1 + self._size(u.left) + self._size(u.right)

    def bf_order(self):
        nodes = [] # empty list
        q = SLLQueue.SLLQueue() # empty queue
        # add root to queue
        if self.r is not None:
            q.add(self.r)
        # while queue is not empty 
        while q.size() > 0:
            # remove next node and add to nodes
            u = q.remove()
            nodes.append(u)
            # check the children
            if u.left is not None:
                q.add(u.left)
            if u.right is not None:
                q.add(u.right)
        return nodes

    def in_order(self) -> list:
        return self._in_order(self.r)

    def _in_order(self, u: Node) -> list:
        nodes = []
        # check if u.left exists
        if u.left is not None:
            # handles left side
            nodes.extend(self._in_order(u.left))
        # add u to nodes
        nodes.append(u)
        # check if u.right exists
        if u.right is not None:
            # handles right side
            nodes.extend(self._in_order(u.right))
        return nodes

    def post_order(self) -> list:
        return self._post_order(self.r)

    def _post_order(self, u: Node):
        nodes = []
        # check if u.left exists
        if u.left is not None:
            # handles left side
            nodes.extend(self._post_order(u.left))
        # check if u.right exists
        if u.right is not None:
            # handles right side
            nodes.extend(self._post_order(u.right))
        # add u to nodes
        nodes.append(u)
        return nodes

    def pre_order(self) -> list:
        return self._pre_order(self.r)

    def _pre_order(self, u: Node):
        nodes = []
        # add u to nodes
        nodes.append(u)
        # check if u.left exists
        if u.left is not None:
            # handles left side
            nodes.extend(self._pre_order(u.left))
        # check if u.right exists
        if u.right is not None:
            # handles right side
            nodes.extend(self._pre_order(u.right))
        return nodes

    def __str__(self):
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)