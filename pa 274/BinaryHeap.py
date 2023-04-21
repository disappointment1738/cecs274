import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i - 1) // 2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        # check invariant 
        if len(self.a) == self.n:
            self._resize()
        # append x to heap
        self.a[self.n] = x
        # move element to its correct position in heap
        self._bubble_up_last()
        return True

    def remove(self):
        # check precodition
        if self.n == 0:
            raise IndexError("Can not remove from an empty heap.")
        # store value of root
        x = self.a[0]
        # overwrite root with the last element
        self.a[0] = self.a[self.n - 1]
        # decrement num of nodes by 1
        self.n -= 1
        # move root node to the correct position
        self._trickle_down_root()
        # check invariant
        if 3 * self.n < len(self.a):
            # self._resize()
            pass
        # return removed value
        return x 

    def depth(self, u) -> int:
        for i in range(self.n):
            if self.a[i] == u:
                depth = 0
                # move up the tree until u is the root
                while i > 0:
                    i = parent(i)
                    depth += 1 # increment edge by 1
                return depth

    def height(self) -> int:
        return int(math.log2(self.n))

    def bf_order(self) -> list:
        # check precodition
        if self.n == 0:
            return []
        q = [self.a[0]]
        result = []
        while q:
            node = q.pop(0)
            result.append(node)
            left = left(self.a.tolist().index(node))
            if left < self.n:
                q.append(self.a[left])
            right = right(self.a.tolist().index(node))
            if right < self.n:
                q.append(self.a[right])
        return result

    def in_order(self) -> list:
        result = []
        self.in_order_help(0, result)
        return result

    def in_order_help(self, i: int, result: list):
        if i < self.n:
            self._in_order(left(i), result)
            result.append(self.a[i])
            self._in_order(right(i), result)

    def post_order(self) -> list:
        result = []
        if self.n == 0:
            return result
        self.post_order_help(0, result)
        return result

    def post_order_help(self, i: int, result: list):
        if i >= self.n:
            return
        self._post_order(left(i), result)
        self._post_order(right(i), result)
        result.append(self.a[i])

    def pre_order(self) -> list:
        result = []
        if self.n > 0:
            self.pre_order_help(0, result)
        return result

    def pre_order_help(self, i: int, result: list):
        if i < self.n:
            result.append(self.a[i])
            self.pre_order_help(left(i), result)
            self.pre_order_help(right(i), result)

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1
        parent = parent(i)
        while i > 0 and self.a[i] < self.a[parent]:
            # swap parent and child
            self.a[i], self.a[parent] = self.a[parent], self.a[i] 
            i = parent # update index
            parent = parent(i) # update the new parent

    def _resize(self):
        # create new array with capacity 2n
        b = _new_array(max(1, 2 * self.n))
        # copy the elements from a to b
        for i in range(0, self.n):
            b[i] = self.a[i]
        # assign a to the new array
        self.a = b

    def _trickle_down_root(self):
        i = 0 # current index of element (at root rn)
        # find children
        left = left(i)
        right = right(i)
        # when i is less than some stuff and when a[i] is larger than its kids
        while i < self.n and left < self.n and right <= self.n and (self.a[left] < self.a[i] or self.a[right] < self.a[i]):
            indexes = {i: self.a[i], left: self.a[left], right: self.a[right]}
            # find the minimum element in a[i], a[left], a[right]
            minIdx = min(indexes, key=indexes.get)
            self.a[i], self.a[minIdx] = self.a[minIdx], self.a[i]
            i = minIdx # update index
            # update children for new index i 
            left = left(i)
            right = right(i)

    def __str__(self):
        return str(self.a[0:self.n])