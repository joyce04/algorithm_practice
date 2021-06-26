# fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ....

def fibonacci_loop(n):
  prev = 0
  current = 1
  for i in range(2, n+1):
    result = prev + current
    prev = current
    current = result
  return result

def fibonacci_array(n):
  arr = [0, 1]
  for i in range(2, n+1):
    arr.append(arr[i-2] + arr[i-1])
  return arr[n]

def fibonacci_recursive(n):
  # O(2^n) : exponential
  # not ideal

  # if n == 0:
  #   return 0
  # elif n == 1:
  #   return 1
  if n < 2:
    return n
  
  return fibonacci_recursive(n-1) +  fibonacci_recursive(n-2)

print(fibonacci_loop(5))
print(fibonacci_array(5))
print(fibonacci_recursive(5))

print(fibonacci_loop(40))
print(fibonacci_array(40))
print(fibonacci_recursive(40))