#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:36:05 2018

@author: grace
"""
import kmp
import aho_corasick

# naive approach
def naive_find_string(text, pattern):
    """Return the found pattern in text.
#    >>> naive_find_string('Hello world', 'llo w')
#    3
#    >>> naive_find_string('Hello world', 'notfound')
#    -1
    """
    text_size = len(text)
    pattern_size = len(pattern)
    
    for i in range(text_size-pattern_size):
        finded = True
        for j in range(pattern_size):
          if text[i+j] != pattern[j]:
              finded = False
              continue
          
        if(finded):
            return i+1
    return -1
            
# Baker-Bird Algorithm for 2D pattern matching
"""
interleave aho_corasick and kmp to find matching 2D pattern with extra space of O(n)
"""
def matching(text_m, pattern_m):
    """
#    >>> matching([list('aabbaaabba'),list('aaabbaaabb'),list('ababaababa')], [list('aab'),list('aaa'),list('aba')])
#    [{2: 2}, {2: 7}]
#    >>> matching([list('abababababababababab'), list('bababababbababababba'), list('aaabababbbababababab'), list('abababbbabababababab'), list('ababbabbbababaaababa'), list('ababbabaabababababba'), list('babababbaabaabbababa'), list('bbababbababababababa'), list('bbbababbababaaababab'), list('bbbababbabababaababa'), list('bbababaababababababa'), list('ababababababababbaba'), list('ababbabababababababa'), list('babbabababababababab'), list('bababaababbababababa'), list('bababababababaabbaba'), list('ababbabababababababa'), list('aabababbbbababbaabaa'), list('aabababbabababbabbbb'), list('bbabababababababbaba')], [list('aba'), list('aba'), list('bab')])
#    [{4: 12}, {4: 18}, {6: 2}, {8: 11}, {8: 17}, {8: 19}, {10: 5}, {10: 10}, {10: 12}, {12: 6}, {13: 2}, {13: 19}, {15: 8}, {16: 3}, {17: 11}, {17: 13}, {19: 3}, {19: 5}]
    """
    search_result = []
    column_result = [0]*len(text_m[0])
    
    row_patterns = [''.join(l) for l in pattern_m]
    # get pattern's trie value by aho_corasick and kmp_failure_table of the trie
    kmp_pattern = list(map(lambda x: str(x), [aho_corasick.search(''.join(line), row_patterns)[-1] for line in pattern_m]))
    # since using the same kmp_prefix function table, only need to trigger once
    kmp_prefix = kmp.make_prefix_func(kmp_pattern)

#    # iterate each row and find patterns with aho_corasick    
    for row_i, text in enumerate(text_m):
        pattern_search = list(map(lambda x: str(x), aho_corasick.search(''.join(text), row_patterns)))
        
#       # iterate with kmp_pattern to keep track of kmp matching results for each column
        for col_i, row_c in enumerate(pattern_search):
            while(column_result[col_i]>0 and row_c!=kmp_pattern[column_result[col_i]]):
                column_result[col_i] = kmp_prefix[column_result[col_i]-1]
            
            if row_c == kmp_pattern[column_result[col_i]]:
                if column_result[col_i] == len(kmp_prefix)-1:
                    # if all match is found, add to search result
                    search_result.append((row_i,col_i))
                    column_result[col_i] = kmp_prefix[column_result[col_i]]
                else:
                    column_result[col_i] += 1
            else:
                column_result[col_i] = kmp_prefix[column_result[col_i]-1]
    return search_result

#import doctest 
#doctest.testmod()