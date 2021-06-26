#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:11:54 2018

@author: grace
"""
# checker program to validate baker-bird algorithm
import baker_bird
import sys
import io
import re

def naive_matching(text_m, pattern_m):
    matching = []
    
    text_size = len(text_m)
    pattern_size = len(pattern_m)
    
    for i in range(text_size-pattern_size+1):
        for j in range(text_size-pattern_size+1):
            found = True
            for y in range(pattern_size):
                for x in range(pattern_size):
                
                  if text_m[i+y][j+x] != pattern_m[y][x]:
                      found = False
          
            if(found):
                matching.append((i+pattern_size-1, j+pattern_size-1))
    return matching

# check if all necessary files are given
if len(sys.argv) != 4:
    print("Usage : python checker.py <input> <output> <checker_output>")
    exit(1)

# read input file
buf = None
try:
    input_file = open(sys.argv[1], 'r')
    buf = io.StringIO(input_file.read())
except:
    print("Unexpected error while reading input file:", sys.exc_info()[0])
else:
    input_file.close()

# process the input
match = re.match(r'(\d+)\s+(\d+)', buf.readline())
p_m = int(match.group(1))
t_n = int(match.group(2))

pattern_m = []
text_m = []
for i in range(p_m):
    pattern_m.append(list(buf.readline().strip()))
for i in range(t_n):
    text_m.append(list(buf.readline().strip()))

# trigger baker-bird
# format of : matching([list('aabbaaabba'),list('aaabbaaabb'),list('ababaababa')], [list('aab'),list('aaa'),list('aba')])
result = baker_bird.matching(text_m, pattern_m)
# write output files
try:
    output_file = open(sys.argv[2], 'w')
    for r in result:
        output_file.write("{} {}\n".format(r[0], r[1]))
except:
    print("Unexpected error while writing output file:", sys.exc_info()[0])
else:
    output_file.close()

# compare with naive_matching
naive_result = naive_matching(text_m, pattern_m)
checker_out_file = open(sys.argv[3], 'w')
if len(naive_result) == len(result) and\
   all(naive_r in result for naive_r in naive_result) and\
   all(r in naive_result for r in result):
        checker_out_file.write('yes')
        print('yes')
else:
    checker_out_file.write('no')
    print('no')
    
checker_out_file.close()
buf.close()
