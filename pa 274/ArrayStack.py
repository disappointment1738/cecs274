import numpy as np
from Interfaces import Stack
from Interfaces import List


class ArrayStack(Stack, List):
    '''
        ArrayStack: Implementation of the Stack interface based on Arrays. 
        All the @abstractemthods should be implemented. 
        An instance of ArrayStack has access to all the methods in ArrayStack and 
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple, 
        s = ArrayStack()
        print(s)
        print(len(s))
    '''
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)
    
    def resize(self):
        '''
            Resize the array
        '''
        # create new array with double capacity
        self.b = self.new_array(max(1, 2 * self.n))
        # copy elements from a into the new array
        for i in range(0, self.n):
            self.b[i] = self.a[i]
        # reassign a to reference the new array
        self.a = self.b

    def get(self, i : int) -> object:
        """return the value of the element i in the List"""
        # check if i is a valid input
        if i < 0 or i >= self.n: 
            raise IndexError()
        # return value in a at index i
        return self.a[i]
    
    def set(self, i : int, x : object) -> object:
        """set the value of the element at the i-th position to be x
        returns the value of teh element that was replaced"""
        # check if i is a valid input
        if i < 0 or i >= self.n: 
            raise IndexError()
        old = self.a[i] # temp variable
        # replace the element
        self.a[i] = x
        return old
    
    def add(self, i: int, x : object) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        # check if i is a valid input
        if i < 0 or i >= self.n: 
            raise IndexError()
        # check if the invariant holds. if it doesn't, resize the list
        if len(self.a) == self.n:
            self.a.resize()
        # shifting forward loop
        for i in range(self.n-1, i, -1):
            self.a[i+1] = self.a[i]
        self.a[i] = x # overwriting new value
        self.n = self.n + 1 # incrementing num of elements

    def remove(self, i : int) -> object :
        '''
            remove element i and shift all j > i one 
            position to the left
        '''
        # check if i is a valid input
        if i < 0 or i >= self.n: 
            raise IndexError()
        # set temp variable 
        x = self.a[i]
        # removing loop
        for i in range(i, self.n-1):
            self.a[i] = self.a[i+1]
        n  = n -1
        # check if the invariant holds. if it doesn't, resize the list
        if len(self.a) == self.n:
            self.a.resize()

    def push(self, x : object) :
        self.add(self.n, x)
    
    def pop(self) -> object :
        return self.remove(self.n-1)

    def size(self) :
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n
        
    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
            Initialize the iterator. It is to be use in for loop
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
            Move to the next item. It is to be use in for loop
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
        




