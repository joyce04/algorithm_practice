# https://leetcode.com/problems/rotate-array/description/
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Could you do it in-place with O(1) extra space?

def rotate_array(arr, k):
  if len(arr) < 2:
    return arr

  for kk in range(k):
    rigth_most = arr[-1]
    for i in range(len(arr)-1, 0, -1):
      arr[i] = arr[i-1]
    arr[0] = rigth_most
    return arr

def rotate_array_inplace(arr, k):
  if len(arr) < 2:
    return arr

  if k > len(arr):
    k = k - len(arr)
  
  k_items  = arr[len(arr)-k:].copy()
  for i in range(len(arr)-k-1, -1, -1):
    arr[i+k] = arr[i]
  for j in range(k):
    arr[j] = k_items[j]
  
  return arr

def rotate_array_short(arr, k):
  arr[:] = arr[len(arr)-k:] + arr[:len(arr)-k]
  return arr



# print(rotate_array([1,2,3,4,5,6,7], 3))
print(rotate_array_inplace([1,2,3,4,5,6,7], 3))
print(rotate_array_inplace([-1], 2))
print(rotate_array_inplace([1,2], 3))
print(rotate_array([1,2], 3))