#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:29:47 2018

@author: grace
"""

import baker_bird
import sys
import io
import re

# check if all necessary files are given
if len(sys.argv) != 3:
    print("Usage : python hw1.py <input> <output>")
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
        print(r)
        output_file.write("{} {}\n".format(r[0], r[1]))
except:
    print("Unexpected error while writing output file:", sys.exc_info()[0])
else:
    output_file.close()

buf.close()

