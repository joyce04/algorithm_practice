# function that reverse a string

def reverse(string):
  # check input
  if not string or type(string)!=str:
    raise Exception('no string given')
  if len(string) < 2:
    return string

  reverse_string = []
  for i in range(len(string)-1, -1, -1):
    reverse_string.append(string[i])
  return ''.join(reverse_string)

def reverse2(string):
  # list[<start>:<stop>:<step>]
  if not string or type(string)!=str:
    raise Exception('no string given')
  if len(string) < 2:
    return string

  return string[::-1]


print(reverse('hello world'))
print(reverse2('hello world'))

print(reverse('h'))
print(reverse(3))
print(reverse(None))