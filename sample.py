"""
MODULE 1 LAB ACTIVITIES

Lab for week 1, spring 2023
"""

"""
INTERFACES

1. (1 pt) Explain the difference between a data structure’s interface and its implementation.
2. (1 pt) True or False: An interface is also referred to as an abstract data type.
3. (1 pt) True or False: If two or more data structures implement a same interface, then they
will have the same functionalities and same run-time efficiencies.

4. (a) (2 pts) Complete the sample project and submit it to the appropriate CodePost folder.
The score you receive on CodePost will be the number of points you receive for this part
of the lab activities. You can find directions for the sample project under Beachboard »
Content » Module 1.

(b) (1 pt) Research: What is the purpose of from ... in each import statement of the
header to the main.py file?
from Spider import Spider
from Ant import Ant
from Board import Board

(c) (1 pt) Research: Notice that both the Ant and Spider classes seem to take arguments
Insect and MobileCritter in the declaration of the class:
class Ant(Insect, MobileCritter):
...
class Spider(Insect, MobileCritter):
...
What is this syntax actually indicating?


5. (1 pt) A UML (Unified Modeling Language) diagram depicts the relationships between two
or more classes, data structures, interfaces, etc. in a program design. The symbol used to
denote interface implementation is a dashed arrow with open tip from the data structure
or class to the interface. For example, the UML diagram for the sample project would look
like the following:

This diagram says that the Ant and Spider classes implement the methods of the MobileCritter
interface. Hence, if we instantiate an Ant or Spider object, we are expecting to be able to
call any of the methods listed in the MobileCritter interface on the object. Moreover, Ant
and Spider override the __str__ method, i.e., they define the string that should be returned
when the function str() is called on an object of the class.
Now, consider the UML diagram below:

(a) (1 pt) True or False: The methods listed in the Queue interface are fully implemented.
(b) (1 pt) What methods does the ArrayQueue data structure implement?
(c) (1 pt) What methods does the SLLQueue data structure implement?
"""

"""
RUN-TIME

1. (1 pt each) Determine the big-O run-time for each algorithm below.
(a) 

def clone(array):
    # returns a copy of the given array
    copy = []
    for e in array:
        copy.append(e)
    return copy

(b) 
def integer_div(a, b):
    #performs integer division a//b 
    count = 0
    total = b
    while total <= a:
        total += b
        count += 1
    return count

(c) 
def mod(a : int, b : int):
# returns the remainder of a divided by b
    if b <= 0:
        return -100
    quotient = a // b
    return a - quotient * b


2. (1 pts) Which of the following are equivalent to O(N)? Why?
• O(4N)
• O(N + 3P) where P < N/2
• O(N + log N)
• O(N + N log N)
• O(N + M)
"""