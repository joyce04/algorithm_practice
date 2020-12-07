# given 2 arrays, create a function that returns whether these arrays contain any common item

# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'i']
# return false

# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'x']
# return true

# 2 parametesr? always arrays?
# return true or false

# how large arrays can be?
# 2 arrays no size limit

# 1. two arrays in nested loop (brute-force) : O(n^2) = O(a*b) & space complexity O(1)

# 2. hashtable? O(a+b) & space complexity O(a)
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']
array3 = ['i', 'j', 'j']
array4 = [1, 2, 3]

def common_item(arr1, arr2):
  hash1 = {x:True for x in array1}
  
  for ch in arr2:
    if hash1.get(ch):
      return True
  return False

print(common_item(array1, array2))
print(common_item(array1, array3))
print(common_item(array3, array4))
print(common_item([], array3))
# print(common_item(array1, array3))

