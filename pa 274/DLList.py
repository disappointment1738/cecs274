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
            for k in range(i):
                p = p.next
        else: # if i is in second half, start at the tail of the list and work backwards
            p = self.dummy
            for k in range(self.n - i):
                p = p.prev
        return p

    def get(self, i) -> object:
        # check precondition
        if i < 0 or i >= self.n:
            raise IndexError()
        # get i-th node using get_node(i)
        u = self.get_node(i)
        # return the data in the i-th node
        return u.x

    def set(self, i: int, x: object) -> object:
        # check precondition 
        if i < 0 or i >= self.n:
            raise IndexError()
        # get the i-th node
        node = self.get_node(i)
        # assign the current data in node i in a temp variable, will be replaced and returned 
        old = node.x
        # set the data in the i-th node to be x
        node.x = x
        # return old value
        return old

    def add_before(self, w: Node, x: object) -> Node:
        # check precondition
        if w is None:
            raise IndexError()
        # create new node `u` with data x
        u = self.Node(x)
        # update the references for nodes
        # for new node u
        u.prev = w.prev 
        u.next = w
        # for node w
        w.prev = u
        # node previous to u
        u.prev.next = u
        # increment num of nodes by 1
        self.n += 1
        return u

    def add(self, i: int, x: object):
        # check precondition
        if i < 0 or i > self.n:
            raise IndexError()
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        # check precondition
        if self.n == 0:
            raise IndexError()
        # update the references for w
        w.prev.next = w.next
        w.next.prev = w.prev
        # decrement num of nodes
        self.n -= 1
        return w.x # return the data in node w

    def remove(self, i: int):
        if i < 0 or i > self.n:  raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        # if the size is 0 or 1, is automatically true
        if self.n == 0 or self.n == 1:
            return True
        # compare 2 letters at the same time to check if they are the same
        else:
            forward = self.dummy.next
            backward = self.dummy.prev
            for i in range(self.n // 2):
                # compare 2 letters at the same time
                if forward.x == backward.x:
                    forward = forward.next
                    backward = backward.prev
                else:
                    return False # if different, it is not a palindrome, so return false
            return True

    def reverse(self):
        # assign head to temp variable
        current = self.dummy.next
        # traverse through list and swap pointers 
        while current is not self.dummy:
            current.next, current.prev = current.prev, current.next # swap pointers
            current = current.prev
        # when reach tail, swap head and tail pointers
        self.dummy.next, self.dummy.prev = self.dummy.prev, self.dummy.next
        index = self.dummy.next

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
