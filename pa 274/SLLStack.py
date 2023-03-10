from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def push(self, x: object):
        # create a new node `u` storing data
        u = self.Node(x)
        # assign the node after `u` to be the head
        u.next = self.head
        # assign `u` as the new head
        self.head = u
        # check the invartiant: does the tail need to be updated?
        if self.n == 0:
            self.tail = u
        # increment num of nodes by 1
        self.n += 1

    def pop(self) -> object:
        # check the precodition: if n = 0, return nil
        if self.n == 0:
            raise IndexError()
        # temp variable storing value of head, return later
        x = self.head.x
        # remove the `head` by updating the head to be `head.next`
        self.head = self.head.next
        # decrement num of nodes by 1
        self.n -= 1
        # check the invariant: if `n` is 0, update the tail to be nil
        if self.n == 0:
            self.tail = None
        # return the removed value
        return x

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
