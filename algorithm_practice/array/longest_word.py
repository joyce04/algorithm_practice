# https://coderbyte.com/results/joyce8804:Longest%20Word:Python3
# return the largest word in the string

import re 

def LongestWord(sen):

  matches = re.findall('[a-zA-Z0-9]+', sen)
  # matches = sorted(matches, key=lambda x: len(x), reverse=True)
  # return matches[0]
  return max(matches, key=len)


print(LongestWord('123456789 98765432'))