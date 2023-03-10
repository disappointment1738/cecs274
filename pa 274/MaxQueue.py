from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        # NOTE: DLLDeque implements the Deque interface but also inherits all methods from DLList
        self.max_deque = DLLDeque()
    
    def add(self, x: object):
        """
        adds an element to the end of this max queue
        """
        # add to the tail of SLLQueue
        super().add(x)
        # check precondition
        if self.max_deque.n == 0:
            self.max_deque.add_first(x)
        # check if x is larger than max
        elif x > self.max():
            self.max_deque = DLLDeque()
            self.max_deque.add_first(x)
        # otherwise, we need to place the element in DLList in decreasing order and discard any elements in the list that are smaller than x
        else: 
            # remove any elements less than x
            for i in range(1, self.max_deque.n):
                if x > self.max_deque.get_node(self.max_deque.n - 1).x:
                    self.max_deque.remove_last()
            # add element
            self.max_deque.add_last(x)

    def remove(self) -> object:
        """
        removes and returns the element at the head of the max queue
        """
        # check the precondition
        if self.n == 0:
            raise IndexError()
        # store data from head here, will be returned later
        x = self.head.x
        # remove from the head of SLLQueue
        super().remove()
        # check if the thingy removed is greater than the maximum
        if x == self.max():
            self.max_deque.remove_first()
        # return the old data
        return x

    def max(self):
        """
        returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)




"""
# TESTER
mq = MaxQueue()
mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(2)
print("Added:", 2)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")
        
"""