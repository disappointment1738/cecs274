import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # check if n is a valid length
        if self.n < 1:
            raise IndexError()
        # generate a random number
        r = random.randint(0, self.n - 1)
        # store head of the array
        head = self.a[ self.j % len(self.a) ]
        # store random index in array that will be removed and returned later
        removed = self.a[ (self.j + r) % len(self.a) ]
        # put head in the random index
        self.a[ (self.j + r) % len(self.a) ] = head
        # remove the head 
        super().remove()
        # check the invariant
        if len(self.a_) > 3 * len(self.a):
            super.resize()
        # return the removed value
        return removed