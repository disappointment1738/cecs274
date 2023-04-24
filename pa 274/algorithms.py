"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for i in range(len(a)-1):
        if a[i] == x:
            return i
    return None


def binary_search(a: List, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            # update right
            right = mid - 1
        else:
            # update left
            left = mid + 1
    return None


def _merge(a0: List, a1: List, a: List):
    i = 0
    # checks and merges lists together
    while 0 < len(a0) and 0 < len(a1):
        if a0[0] < a1[0]:
            a[i] = a0.pop(0)
        else:
             a[i] = a1.pop(0)
        i += 1
    # when all elements of the other list are copied
    while 0 < len(a0):
         a[i] = a0.pop(0)
         i += 1
    while 0 < len(a1):
        a[i] = a1.pop(0)
        i += 1
    return a


def merge_sort(a: List):
    if len(a) <= 1:
        return a # because it's already sorted
    mid = len(a) // 2
    a0 = a[:mid] # first half of array
    a1 = a[mid:] # second half of array
    # recusively sort
    a0 = merge_sort(a0)
    a1 = merge_sort(a1)
    return _merge(a0, a1, a)


def _quick_sort(a: List, start, end, p = True):
    if start < end:
        if p:
            pIdx = partition(a, start, end)
        else:
            pIdx = partitionDes(a, start, end)
        _quick_sort(a, start, pIdx - 1)
        _quick_sort(a, pIdx + 1, end)


def partition(a: List, start, end):
    pivot = a[start]
    l = start + 1
    r = end
    while l <= r:
        # loop for l
        while a[l] <= pivot:
            l += 1
        # loop for r
        while a[r] > pivot:
            r -= 1
        if l < r:
            # swap a[l] and a[r]
            a[l], a[r] = a[r], a[l]
    # swap pivot and a[r]
    a[start], a[r] = a[r], a[start] # where a[start] is the pivot
    return l

def partitionDes(a: List, start, end):
    """ 
    Does the same thing as parition but it does it from right to left
    """
    pivot = a[end]
    l = start
    r = end - 1
    while l <= r:
        while a[l] >= pivot:
            l += 1
        while a[r] < pivot:
            r -= 1
        if l < r:
            a[l], a[r] = a[r], a[l]
    a[end], a[l] = a[l], a[end]
    return l

def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    _quick_sort(a, 0, len(a) - 1)
    return a
