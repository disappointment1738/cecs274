import numpy as np
import ArrayStack
#import BinaryTree
import ChainedHashTable
#import DLList
#import operator
import re


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable()

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        a = ArrayStack.ArrayStack()
        # checking the parenthesis in string s
        for c in s:
            if c == '(':
                a.push(c)
            elif c == ')':
                # used to ensure that the opening and closing parentheses in the input string s match properly
                if a.size() == 0 or a.pop() != '(':
                    return False
        return a.size() == 0

    def build_parse_tree(self, exp: str) -> str:
        # todo
        pass

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        # todo
        pass

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)

    def print_expression(self, exp):
        # adds all of the variables into one list (given as hint)
        variables = [x for x in re.split('\W+', exp) if x.isalnum()] 
        # creates a list of tokens (everything else that's not a variable) -- given as a hint
        everythingElse = re.split('\w+', exp)
        result = ''
        # concatenating into one string
        for i in range(len(everythingElse)):
            result += everythingElse[i] # adds the not-variable item to the string
            # checks if i isn't too big to not be a variable
            if i < len(variables):
                value = self.dict.find(variables[i]) # this finds the value of the variable at the index i
                    # checks if the value found is valid to be added to the string
                if value is not None:
                    result += str(value)
                # otherwise, add the variable instead since there's not a value for that variable
                else: 
                    result += variables[i]
        print(result)