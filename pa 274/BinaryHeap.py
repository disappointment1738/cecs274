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
            raise IndexError
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
            self._resize()
        # return removed value
        return x 

    def depth(self, u) -> int:
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
        # todo
        pass

    def bf_order(self) -> list:
        # todo
        pass

    def in_order(self) -> list:
        # todo
        pass

    def post_order(self) -> list:
        # todo
        pass

    def pre_order(self) -> list:
        # todo
        pass

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1
        parent = parent(i)
        while i > 0:
            # swap parent and child
            self.a[i], self.a[parent] = self.a[parent], self.a[i] 
            i = parent # update index
            parent = parent(i) # update the new parent

    def _resize(self):
        # create new array with capacity 2n
        b = self._new_array(max(1, 2 * self.n))
        # copy the elements from a to b
        for k in range(0, self.n):
            b[k] = self.a[k]
        # assign a to the new array
        self.a = b

    def _trickle_down_root(self):
        i = 0 # current index of element (at root rn)
        # find children
        left = left(i)
        right = right(i)
        # when i is less than some stuff and when a[i] is larger than its kids
        while i < self.n or i < left or i < right and self.a[left] < self.a[i] or self.a[right] < self.a[i]:
            # find the minimum element in a[i], a[left], a[right]
            minIdx = min(left, right, i)
            self.a[i], self.a[minIdx] = self.a[minIdx], self.a[i]
            i = minIdx # update index
            # update children for new index i 
            left = left(i)
            right = right(i)

    def __str__(self):
        return str(self.a[0:self.n])