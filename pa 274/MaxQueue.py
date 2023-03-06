from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x : object):
        """
        adds an element to the end of this max queue
        INPUT: x the element to add
        """
        # add to SLLQueue
        super().add(x)
        self.max_deque.add_last(0)
        if x > self.max():
            self.max_deque = DLLDeque()
            self.max_deque.add_first(x)
        else:
            # add to max_deque
            self.max_deque.add_last(x)
            while self.max_deque.n > 1 and x > self.max_deque.dummy.prev.x:
                self.max_deque.remove_last()

    def remove(self) -> object:
        """
        removes and returns the element at the head of the max queue
        """
        removedValue = super().remove() #removes from head of SLL
        if self.max_deque.n == 0:
            raise IndexError()
        if removedValue == self.max(): # checks if the max was removed
            self.max_deque.remove_first() #removes head of DLL
        return removedValue

    def max(self):
        """
        returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)