#import numpy as np
import ArrayStack
#import BinaryTree
#import ChainedHashTable
#import DLList
#import operator


class Calculator:
    def __init__(self):
        self.dict = None # ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        a = ArrayStack()
        # iterate through the string to check 
        for i in range(0, len(s)):
            # check if there is a open parenthesis at a part
            if s[i] == '(':
                a.add(i, s[i])
            # check if there is a closed parenthesis at a part
            if s[i] == ')':
                a.remove()
        # if the list is empty, then there's no unmatched parenthesises, which makes the expression valid
        if len(a) == 0:
            return True
        else:
            return False

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
