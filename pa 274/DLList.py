from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        # check precondition
        if i < 0 or i >= self.n:
            return self.dummy
        # if i is in first half, start at head of the list and work forward
        if i < self.n // 2:
            p = self.dummy.next
            for i in range(i):
                p = p.next
        else: # if i is in second half, start at the tail of the list and work backwards
            p = self.dummy.prev
            for i in range(self.n - 1):
                p = p.prev
        return p

    def get(self, i) -> object:
        # todo
        pass

    def set(self, i: int, x: object) -> object:
        # todo
        pass

    def add_before(self, w: Node, x: object) -> Node:
        # todo
        pass

    def add(self, i: int, x: object):
        # todo
        pass

    def _remove(self, w: Node):
        # todo
        pass

    def remove(self, i: int):
        if i < 0 or i > self.n:  raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        # todo
        pass

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
