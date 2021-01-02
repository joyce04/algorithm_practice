# reverse a string 

def reverse_loop(sent):
  n_str = []
  for i in range(len(sent)-1, -1, -1):
    n_str.append(sent[i])
  return ''.join(n_str)

def reverse_recursive(sent):
  size = len(sent)
  if len(sent) == 1:
    return sent
  last_char = sent[size-1]
  return last_char + reverse_recursive(sent[0:size-1])


print(reverse_loop('yoyo mastery'))
print(reverse_recursive('yoyo mastery'))