import numpy as np
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
