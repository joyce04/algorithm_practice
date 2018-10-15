#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 7 13:36:05 2018

@author: grace
"""

# Knuth-Morris-Pratt
"""
 prefix function
 
 j,i(j+1) 
 if pattern[i]==pattern[j] increment both i and j
 else decrement j and recount
"""
def make_prefix_func(pattern):
    """Return built prefix array(table) for given pattern
#    >>> make_prefix_func('abacaaba')
#    [0, 0, 1, 0, 1, 1, 2, 3]
#    >>> make_prefix_func('ababaca')
#    [0, 0, 1, 2, 3, 0, 1]
#    >>> make_prefix_func('ababababca')
#    [0, 0, 1, 2, 3, 4, 5, 6, 0, 1]
    """
    pattern_size = len(pattern)
    prefix_table = [0]
    j = 0
    for i in range(1, pattern_size):
        while(j>0 and pattern[i]!=pattern[j]):
            j = prefix_table[j-1]

        if pattern[i] == pattern[j]:
            j +=1 
        prefix_table.append(j)

    return prefix_table

"""
 search function
 with failure table, start matching with text and pattern
 if unmatching character is found, use failure table to shift based on matching prefix

input: text, pattern
output: array of found index
"""
def search(text, pattern):
    """
#    >>> search('ababacabacaabacaaba', 'ababaca')
#    [6]
#    >>> search('bacabcabcadabc', 'abcabca')
#    [9]
#    >>> search('bacabcabcadabc', 'notfound')
#    []
#    >>> search('bacabcabcadaabcabcadd', 'abcabca')
#    [9, 18]
#    >>> search('bacabcabcabca', 'abcabca')
#    [9, 12]
    """
    prefix_table = make_prefix_func(pattern)
    text_size = len(text)
    pattern_size = len(pattern)
    output = []
    
    j = 0
    for i in range(text_size):
        # when text[i] != pattern[j] -> j-1
        while(j>0 and text[i]!=pattern[j]):
            j = prefix_table[j-1]
        
        # if all match
        if(text[i]==pattern[j]):
            if (j== pattern_size-1):
#                print('found at index %d' % (i- pattern_size + 2))
                output.append(i)
                j = prefix_table[j]
            else:
                j += 1
    return output

#import doctest 
#doctest.testmod()