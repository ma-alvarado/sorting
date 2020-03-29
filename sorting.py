#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''

    i = j = k = 0
    xsys = []
    while i < len(xs) and j < len(ys):
        outcome = cmp(xs[i],ys[j])
        if outcome == -1:
            xsys.append(xs[i])
            i += 1
        if outcome == 1:
            xsys.append(ys[j])
            j += 1
        if outcome == 0:
            xsys.append(xs[i])
            xsys.append(ys[j])
            i += 1
            j += 1
    while i < len(xs):
        xsys.append(xs[i])
        i += 1
    while j < len(ys):
        xsys.append(ys[j])
        j += 1
    
    return xsys

    
    
def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs
    '''
    left = 0
    right = len(xs)

    if len(xs) > 1:
        mid = len(xs) // 2
        lefthalf = xs[0:mid]
        righthalf = xs[mid:]
        
        merge_sorted(lefthalf,cmp=cmp_standard)
        merge_sorted(righthalf,cmp=cmp_standard)
        
        i = j = k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                xs[k] = lefthalf[i]
                i += 1
            else:
                xs[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            xs[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            xs[k] = righthalf[j]
            j += 1
            k += 1
        return xs

def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs
    
    This is a test
    '''


def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented in-place,
    i.e. with O(1) memory requirement.
    Merge sort, on the other hand, has an O(n) memory requirement.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable instead of returning a copy of the list.
    '''
