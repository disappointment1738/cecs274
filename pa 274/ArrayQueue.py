import numpy as np
from Interfaces import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, object)

    def resize(self):
        '''
            Resize the array
        '''
        # create new array with capacity 2n
        self.b = new_array(min(1, 2 * self.n))
        # copy the elements from a to b
        for k in range(0,n):
            self.b[k] = a[ (self.j + k) % len(self.a) ]
        # assign a to the new array
        self.a = self.b
        # set the head of the index, j, to 0.
        self.j = 0

    def add(self, x: object):
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        # check the invariant (n <= len(a) <= 3n)
        if len(self.a) == self.n:
            self.resize()
        # add x to the backing array at index j+n mod len(a) (i.e., at the tail)
        self.a[ (self.j + self.n) % len(self.a) ] = x
        # increment by 1
        self.n = self.n + 1

    def remove(self) -> object:
        '''
            remove the first element in the queue
        '''
        # check if i is a valic input
        if self.n <= 0:
            raise IndexError()
        # temp variable to store value that will be removed
        x = self.a[self.j]
        # increment j by 1 mod len(a)
        self.j = (self.j + 1) % len(self.a)
        # decrement n by 1
        self.n = self.n - 1
        # check if the invariant holds
        if len(self.a) > 3 * self.n:
            self.resize()
        # return the value that was removed
        return x

    def size(self):
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
