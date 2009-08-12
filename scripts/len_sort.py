#!/usr/bin/python
"""
len_sort.py - so kanzure can figure out some ridiculously long names used for genes
"""

def bylength(word1, word2):
    """
    write your own compare function:
    returns value > 0 of word1 longer then word2
    returns value = 0 if the same length
    returns value < 0 of word2 longer than word1
    """
    return len(word1) - len(word2)

