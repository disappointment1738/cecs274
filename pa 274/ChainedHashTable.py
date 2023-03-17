from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: int) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        # determine the bin of the list where the item is stored
        bin = self._hash(key)
        # iterate over the list at that bin index and check if the keys match (return value if they do)
        for i in range(self.t[bin].size() - 1):
            if self.t[bin].get(i).value:
                return self.t[bin].get(i).value
        # return None if the loop doesn't return anything, then none of the keys match
        return None

    def add(self, key: object, value: object):
        # check the precondition: if item with key exists, return false
        if self.find(key)!= None:
            return False
        # check the invariant: do we need to resize?
        if self.n == len(self.t):
            self.resize()
        # bin index
        bin = self._hash(key)
        # create a new node with key and val
        item = self.Node(key, value)
        # insert the new node to the start of the list the bin memory index (t[has_code(key)])
        self.t[bin].add(0, item)
        # increment num of elements by 1
        self.n += 1
        return True

    def remove(self, key: int) -> object:
        # find the bin index where the node with the given key should be stored
        bin = self._hash(key)
        # iterate over the nodes in that bin, and check if the item key matches the given key
        for i in range(self.t[bin].size() - 1):
            self.t[bin].remove(i)
            self.n -= 1 # decrement num of elements by 1
            # check the invariant
            if len(self.t) > 3 * self.n: 
                self.resize()
        # return false if nothing matched because there is nothing to remove
        return False

    def resize(self):
        # check the num of items in the table is the same as the num of bins.
        # if same, double the num of bins
        if self.n == len(self.t):
            self.d += 1
        # otherwise, create temp with half of num of bins
        else:
            self.d -= 1
        # create new temp table
        temp = self.alloc_temp(2 ** self.d)
        # copy every list in table t into the table temp
        for j in range(len(self.t) - 1):
            for i in range(self.t[j].size() - 1):
                bin = self._hash(self.t[j].get(i).key)
        # reassign t to temp
        self.t = temp

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"
