"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for i in range(len(a)-1):
        if a[i] == x:
            return i
    return -100


def binary_search(a: List, x):
    left = 0
    right = len(a) - 1
    binary_help(a, left, right, x)


def binary_help(a: list, left: int, right: int, x):
    """
    Helper method for binary_search that uses recursion to search through the list.
    """
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            # update right
            right = mid - 1
            # search the first half
            binary_help(a, left, right, x)
        else:
            # update left
            left = mid + 1
            # search the second half
            binary_help(a, left, right, x)
    return -100


def _merge(a0: List, a1: List, a: List):
    i0 =0 # current index of a0
    i1= 0 # current index of a1
    for i in range(len(a)-1):
        if i0 == len(a0): # we copied all elements from a0
            a[i] = a1[i1]
            i1 += 1
        elif i1 == len(a1): # we copied all elements from a1
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1


def merge_sort(a: List):
    if len(a) <= 1:
        return a # because it's already sorted
    mid = len(a) // 2
    a0 = a[:mid-1] # first half of array
    a1 = a[mid:] # second half of array
    # recusively sort
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)


def _quick_sort_f(a: List, start, end):
    # todo
    pass


def _quick_sort_r(a: List, start, end):
    # todo
    pass


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)
