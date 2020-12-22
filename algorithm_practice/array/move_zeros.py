# https://leetcode.com/problems/move-zeroes/description/
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# must do in-place

# input [0, 1, 0, 3, 12]
# output [1, 3, 12, 0, 0]

def move_zeros(arr):
  # easiest 
  for i in range(len(arr)):
    if arr[i]==0:
      for j in range(i, len(arr)-1):
        arr[j] = arr[j+1]
      arr[j+1] = 0
  return arr

def move_zeros_b(arr):
  # bubble flip
  # 0 1 0 3 12
  # i j
  # 1 0 0 3 12
  #   i   j
  # 1 3 0 0 12
  #     i   j
  if len(arr)<2:
    return arr

  i = 0
  j = 1
  while(j < len(arr) and i < len(arr)):
    if arr[i]==0:
      if arr[j]!=0:
        arr[i] = arr[j]
        arr[j] = 0
        i += 1
        j += 1
      else:
        j += 1
    else:
      i += 1
      j += 1
    
  return arr

# print(move_zeros([0, 1, 0, 3, 12]))
# print(move_zeros_b([0, 1, 0, 3, 12]))
# print(move_zeros_b([2, 1]))
print(move_zeros_b([4,2,4,0,0,3,0,5,1,0]))
