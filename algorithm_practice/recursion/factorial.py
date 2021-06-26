# def that finds the factorial of any number

def factorial_loop(num):
  total = 1
  for i in range(num, 1, -1):
    total *= i
  return total

def factorial_recursive(num):
  if num == 2:
    return 2
  else:
    return num * factorial_recursive(num-1)

print(5*4*3*2*1)
print(factorial_loop(5))
print(factorial_recursive(5))
