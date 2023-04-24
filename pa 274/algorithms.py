"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return None


def binary_search(a: List, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r)//2
        if x == a[m]:
            return m
        elif x < a[m]:
            r = m - 1 # update right
        else:
            l = m + 1 # update left
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
    # when alll elements of the other lists are copied
    while 0 < len(a0):
         a[i] = a0.pop(0)
         i += 1
    while 0 < len(a1):
        a[i] = a1.pop(0)
        i += 1
    return a


def merge_sort(a: List):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    # recursively sort
    a0 = merge_sort(a[0:mid]) # first half
    a1 = merge_sort(a[mid:len(a)]) # second half
    return _merge(a0, a1, a)


def partition(a: List, start, end):
    pivot = a[start]
    l = start + 1
    r = end
    while l <= r:
        # loop for l
        while l <= r and a[l] <= pivot:
            l += 1
        # loop for r
        while l <= r and a[r] > pivot:
            r -= 1
        if l < r:
            a[l], a[r] = a[r], a[l]
    a[start], a[r] = a[r], a[start]
    return r


def _quick_sort(a: List, start, end, p = True):
    if start < end:
        if p:
            p_idx = partition(a, start, end)
        else:
            p_idx = partition_desc(a, start, end)
        _quick_sort(a, start, p_idx - 1)
        _quick_sort(a, p_idx + 1, end)


def partition_desc(a: List, start, end):
    pivot = a[end]
    l = start
    r = end - 1
    while l <= r:
        # loop for l
        while l <= r and a[l] >= pivot:
            l += 1
        # loop for r
        while l <= r and a[r] < pivot:
            r -= 1
        if l < r:
            a[l], a[r] = a[r], a[l]
    a[end], a[l] = a[l], a[end]
    return l


def quick_sort(a: List, p = True):
    _quick_sort(a, 0, len(a) - 1)
    return a
